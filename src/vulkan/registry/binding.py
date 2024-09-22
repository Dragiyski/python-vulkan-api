import ast, types, ctypes, sys
from os import linesep
from logging import getLogger
from types import SimpleNamespace
from threading import RLock
import pycparser.c_ast
from enum import IntEnum, IntFlag
from ._nodes import nodes, bit_enum_map, enum_bit_map, category_name_map, enum_value_map, value_enum_map
from .platform import macro_ignore, platform_types, native_types
from .xml_parser import Node

_vulkan_extension_base = 1000000000
_handle_nd_ctype = ctypes.c_void_p if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_uint64

logger = getLogger('vulkan.registry')

class Binding:
    def __init__(self):
        from ._c import CContext
        self.c_context = CContext()
        c_type = set()
        c_type.update(category_name_map['struct'])
        c_type.update(category_name_map['union'])
        c_type.update(category_name_map['handle'])
        c_type.update(category_name_map['enum'])
        c_type.update(category_name_map['bitmask'])
        c_type.update({ k for k in category_name_map['alias'] for n in nodes[k] if n.has_attribute('alias') and n.get_attribute('alias') in self.c_context.c_type_set })
        self.c_context.c_type_set.update(c_type)
        self.c_context.c_type_map.update(platform_types)
        self.c_context.c_type_map.update(native_types)
        self._names = set(c_type)
        self._names.update(category_name_map['value'])
        self._names.update(category_name_map['alias'])
        self._names.update({ x[len('PFN_'):] if x.startswith('PFN_') else x for x in category_name_map['callback'] })
        self._names.update(category_name_map['command'])
        self._complex_type_resolver_lock = RLock()
        self._resolving_complex_types = {}
        self._complex_types = {}
        for name in category_name_map['define']:
            if name in macro_ignore:
                continue
            node_set = nodes[name]
            for node in node_set:
                if node.get_path()[-2:] != ['types', 'type']:
                    continue
                try:
                    self.c_context.define(node.get_text())
                except self.c_context.DefinitionError:
                    pass
        for name in self.c_context.pp_value_code:
            try:
                self.__dict__[name] = self.c_context.get_constant_value(name)
                self._names.add(name)
            except NotImplementedError:
                pass
        macro_ast_def = {}
        for name in self.c_context.pp_func_code:
            try:
                macro_ast_def[name] = self.c_context.get_python_code_for_func_macro(name)
            except NotImplementedError:
                pass
        macro_ast_module = ast.Module(list(macro_ast_def.values()))
        ast.fix_missing_locations(macro_ast_module)
        vulkan_macros = {}
        exec(compile(macro_ast_module, '<vulkan.registry.#define>', 'exec'), vulkan_macros)
        for name in macro_ast_def.keys():
            self.__dict__[name] = vulkan_macros[name]
            self._names.add(name)
        pass

    def __dir__(self):
        return object.__dir__(self) + list(self._names)
    
    def __getattr__(self, name: str):
        try:
            return self.__getitem__(name)
        except KeyError:
            raise AttributeError(name)

    def __getitem__(self, name: str):
        if name in self._names:
            if name in self.__dict__:
                return self.__dict__[name]
            try:
                value = self._get_binding(name)
            except NotImplementedError:
                logger.warning(sys.exc_info(), exc_info=True)
                raise KeyError(name)
            self.__dict__[name] = value
            return value
        raise KeyError(name)
    
    def _get_binding(self, name):
        if name not in self._names:
            raise KeyError(name)
        name = self._resolve_alias(name)
        if name in category_name_map['value']:
            if name in value_enum_map:
                enum_name = self._resolve_alias(value_enum_map[name])
                if enum_name in bit_enum_map:
                    enum_name = self._resolve_alias(bit_enum_map[enum_name])
                return self[enum_name][name]
            return self._get_vulkan_value(name)
        if name in category_name_map['enum']:
            return self._get_vulkan_enum(name, IntEnum)
        if name in category_name_map['bitmask']:
            return self._get_vulkan_enum(name, IntFlag)
        if name in category_name_map['handle']:
            return self._generate_handle_class(name)
        # Note: some callbacks might require structure processing, while some structure might require callback
        if f'PFN_{name}' in category_name_map['callback']:
            return self._generate_callback_type(name)
        if name in category_name_map['struct'] or name in category_name_map['union']:
            return self._generate_complex_type(name)
        raise NotImplementedError('No vulkan binding for "%s"' % name)
    
    def _resolve_alias(self, name):
        while name in category_name_map['alias']:
            for node in nodes[name]:
                if node.has_attribute('alias'):
                    name = node.get_attribute('alias')
        return name
    
    def _get_vulkan_value(self, name):
        for node in nodes[name]:
            if node.has_attribute('bitpos'):
                bitpos = self.c_context.c_parser.parse_c_int(node.get_attribute('bitpos'))
                if bitpos < 0 or bitpos >= 64:
                    raise ValueError('Invalid bit position: expected value in range [0; 64)')
                return 1 << bitpos
            if node.has_attribute('value'):
                value = self.c_context.get_constant_value(node.get_attribute('value'))
            elif node.has_attribute('offset'):
                offset = self.c_context.c_parser.parse_c_int(node.get_attribute('offset'))
                ext_number = None
                if node.has_attribute('extnumber'):
                    ext_number = self.c_context.c_parser.parse_c_int(node.get_attribute('extnumber'))
                else:
                    ext_node = None
                    ancestor_node = node.parent_node
                    while ancestor_node is not None:
                        if ancestor_node.node_name == 'extension':
                            ext_node = ancestor_node
                            break
                        ancestor_node = ancestor_node.parent_node
                    if ext_node is None:
                        raise ValueError(f'Missing extension number for @offset defined value: {name}')
                    if not ext_node.has_attribute('number'):
                        ext_name = ext_node.get_attribute('name')
                        if ext_name is None:
                            ext_name = f'Node at {ext_node.file_path}'
                        raise ValueError(f'Missing extension @number for extension {ext_name} while lookup value for {name}')
                    ext_number = self.c_context.c_parser.parse_c_int(ext_node.get_attribute('number'))
                value = _vulkan_extension_base + (ext_number - 1) * 1000 + offset
            else:
                continue
            if node.get_attribute('dir') == '-':
                value = -value
            return value
        raise NotImplementedError(f'No node defines a value for "{name}"')
    
    def _get_vulkan_enum(self, enum_name, base_class):
        content_name = enum_name
        if enum_name in enum_bit_map:
            content_name = enum_bit_map[enum_name]
        if content_name not in enum_value_map or len(enum_value_map[content_name]) <= 0:
            # Just an empty enum class for enum?
            return types.new_class(enum_name, (base_class,))
        def _prepare_enum(namespace):
            # While it is possible to just assign the same value for the aliases
            # the name of the alias would depend on the order of the set()
            # Instead, only assign non-alias member first here...
            for name in enum_value_map[content_name]:
                if name in category_name_map['alias']:
                    continue
                namespace[name] = self._get_vulkan_value(name)
        cls = types.new_class(enum_name, (base_class,), None, _prepare_enum)
        # ... and then declare alias members after the class __prepare__ has been called.
        for name in enum_value_map[content_name]:
            if name in category_name_map['alias']:
                alias_name = self._resolve_alias(name)
                if alias_name != name:
                    assert hasattr(cls, alias_name), 'hasattr(cls, alias_name)'
                    setattr(cls, name, getattr(cls, alias_name))
        return cls
    
    def _generate_handle_class(self, name: str):
        # Direct binding won't have some fancy handle processing, instead that is left to the user
        # or other bindings using the direct binding. Instead the only thing this binding will do
        # is ensure a properly named class is returned.
        for node in nodes[name]:
            info = { name: name }
            if node.get_path()[-2:] == ['types', 'type'] and node.get_attribute('category') == 'handle':
                handle_type = node.get('type').get_text()
                match handle_type:
                    # Dispatchable handles are just (opaque) pointers in main (host) memory. They are guarateed to be unique for the entire process.
                    case 'VK_DEFINE_HANDLE':
                        handle_base_class = ctypes.c_void_p
                        info['dispatchable'] = True
                    case 'VK_DEFINE_NON_DISPATCHABLE_HANDLE':
                        handle_base_class = _handle_nd_ctype
                        info['dispatchable'] = False
                    case _:
                        raise NotImplementedError('Unexpected handle type "%s" for handle "%s".' % (handle_type, handle_base_class))
                if node.has_attribute('objtypeenum'):
                    info['object_type'] = self[node.get_attribute('objtypeenum')]
                info['parent'] = None
                if node.has_attribute('parent'):
                    info['parent'] = self[node.get_attribute('parent')]
                return type(name, (handle_base_class,), {
                    '_vulkan_': SimpleNamespace(**info)
                })
            pass
        pass

    def _generate_complex_type(self, name):
        cls = self._get_complex_type_class(name)
        for name in self._resolving_complex_types:
            self._resolve_complex_type(name)
        return cls
    
    def _get_complex_type_class(self, name):
        with self._complex_type_resolver_lock:
            if name not in self._complex_types:
                assert name not in self._resolving_complex_types, """name not in self._resolving_complex_types"""
                if name in category_name_map['union']:
                    assert name not in category_name_map['struct'], """name not in category_name_map['struct']"""
                    Class = ctypes.Union
                elif name in category_name_map['struct']:
                    Class = ctypes.Structure
                else:
                    raise ReferenceError(f'Unknown complex type "{name}"')
                if name not in nodes:
                    raise ReferenceError(f'Missing node for complex type "{name}"')
                # (1) Assign all new classes to _complex_types and _resolving_complex_types
                self._complex_types[name] = self._resolving_complex_types[name] = type(name, (Class,), {})
                for node in  nodes[name]:
                    if node.get_path()[-2:] == ['types', 'type'] and node.get_attribute('category') in ['struct', 'union']:
                        for member_node in node.get_all('member'):
                            member_type = member_node.get('type').get_text()
                            if member_type in category_name_map['struct'] or member_type in category_name_map['union']:
                                # (2) Recursively generate subclasses (see (1))
                                self._get_complex_type_class(member_type)
                                # No need for self-check, (1) added the class to the _complex_types, so recursively calling the same name
                                # will already return the new class.
            return self._complex_types[name]
        
    def _resolve_complex_type(self, name):
        if name not in self._resolving_complex_types:
            return
        if name not in nodes:
            raise ReferenceError(f'Missing node for complex type "{name}"')
        for node in  nodes[name]:
            if node.get_path()[-2:] == ['types', 'type'] and node.get_attribute('category') in ['struct', 'union']:
                c_code = ['%s %s {' % (node.get_attribute('category'), name)]
                for member_node in node.get_all('member'):
                    c_code.append('%s;' % member_node.get_text())
                c_code.append('};')
                c_code = linesep.join(c_code)
                c_ast = self.c_context.parse(c_code)
                c_decl = c_ast.ext[0]
                assert isinstance(c_decl.type, pycparser.c_ast.Struct), """isinstance(c_decl.type, pycparser.c_ast.Struct)"""
                assert c_decl.type.name == name, """c_decl.type.name == name"""
                _fields_ = []
                _members_ = {}
                for member_decl in c_decl.type.decls:
                    # member_decl = structural declaration of the named struct/union member;
                    # Decl: <typename> <member_name> becomes: Decl(type=TypeDecl(type=IdentifierType))
                    # Decl: const <typename> *<member_name> becomes: Decl(type=PtrDecl(quals=[], type=TypeDecl(quals=['const'], type=IdentifierType)))
                    # Decl: const <typename> const *<member_name> becomes: Decl(type=PtrDecl(quals=['const'], type=TypeDecl(quals=['const'], type=IdentifierType)))
                    # Decl: const char* const* becoms: Decl(type=PtrDecl(quals=[], type=PtrDecl(quals=['const'], type=TypeDecl(quals=['const'], type=IdentifierType))))
                    pass
                pass
        pass