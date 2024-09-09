import ast, types
from types import MappingProxyType
from enum import IntEnum, IntFlag
import pycparser.c_ast
from ._nodes import nodes, bit_enum_map, enum_bit_map, category_name_map, enum_value_map, value_enum_map
from .platform import macro_ignore, platform_types, native_types
from .xml_parser import Node

vulkan_extension_base = 1000000000

class Binding:
    def __init__(self):
        from ._c import CContext
        self.c_context = CContext()
        self.c_context.c_type.update(category_name_map['type'])
        self.c_context.c_type.update(category_name_map['struct'])
        self.c_context.c_type.update(category_name_map['union'])
        self.c_context.c_type.update(category_name_map['handle'])
        self.c_context.c_type.update(category_name_map['enum'])
        self.c_context.c_type.update(category_name_map['bitmask'])
        self.c_context.c_type.update({ k for k in category_name_map['alias'] for n in nodes[k] if n.has_attribute('alias') and n.get_attribute('alias') in self.c_context.c_type })
        self._names = set(self.c_context.c_type)
        self._names.update(category_name_map['value'])
        self._names.update(category_name_map['alias'])
        self._names.update(category_name_map['callback'])
        self._names.update(category_name_map['command'])
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
                value = vulkan_extension_base + (ext_number - 1) + offset
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
            for name in enum_value_map[content_name]:
                value_name = self._resolve_alias(name)
                namespace[name] = self._get_vulkan_value(value_name)
        return types.new_class(enum_name, (base_class,), None, _prepare_enum)