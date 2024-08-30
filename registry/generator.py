import ctypes
import ast
import re
from collections import OrderedDict
from pathlib import Path
from .context import Context
from .platform import CPlainType, CPointerType, CArrayType, CComplexType, CFunctionType
from os import linesep

enum_class_suffix = {
    'enum': 'Enum',
    'bitmask': 'Flag',
    None: ''
}

enum_base_class = {
    'enum': 'IntEnum',
    'bitmask': 'IntFlag',
    None: 'int'
}

ctypes_types = [name for name in dir(ctypes) if name.startswith('c_')]

def module_sorted(modules):
    return sorted([m for m in modules if not m.startswith('.')]) + sorted([m for m in modules if m.startswith('.')])

class GeneratorError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.__dict__.update(**kwargs)

class GeneratedModule:
    def __init__(self, path: list):
        self.path = path
        self.lines = []
        self.deps = {}

    def add_dep(self, module: str, selector: str | bool):
        if module not in self.deps:
            self.deps[module] = {}
        if selector not in self.deps[module]:
            self.deps[module][selector] = False

    def flush_dep(self):
        is_import = False
        for mod in module_sorted(self.deps.keys()):
            ns = self.deps[mod]
            if False in ns and not ns[False]:
                self.lines.append('import %s' % mod)
                is_import = True
                ns[False] = True
            if True in ns and not ns[True]:
                self.lines.append('from %s import *' % mod)
                is_import = True
                ns[True] = True
            names = {k: v for k, v in ns.items() if isinstance(k, str) and not v}
            if len(names) > 3:
                is_import = True
                self.lines.append('from %s import (' % mod)
                for name in sorted(names):
                    self.lines.append('    %s,' % name)
                    ns[name] = True
                self.lines.append(')')
            elif len(names) > 0:
                self.lines.append('from %s import %s' % (mod, ', '.join(sorted(names.keys()))))
                is_import = True
                for name in names:
                    ns[name] = True
        if is_import:
            self.lines.append('')
    
    def update_file(self, base_path: Path):
        path = base_path.joinpath('/'.join(self.path) + '.py')
        path.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(path, 'w') as stream:
            stream.write(linesep.join(self.lines))


class Generator:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir).resolve()
        self.base_dir: Path

    def _create_function_source(self, context: Context, name: str, module: GeneratedModule, *, loc_type='.._vulkan_type', loc_callback='.._vulkan_callback'):
        def check_type_dep(ctype):
            if isinstance(ctype, CPointerType):
                check_type_dep(ctype.deref())
            elif isinstance(ctype, CArrayType):
                check_type_dep(ctype.item_ctype)
            elif isinstance(ctype, CComplexType):
                module.add_dep('%s.%s' % (loc_type, ctype.name), ctype.name)
            elif isinstance(ctype, CFunctionType):
                module.add_dep('%s.%s' % (loc_callback, ctype.name), ctype.name)

        ctype = context.ctypes_map[name]
        module.add_dep('ctypes', False)
        module.add_dep('..._ctypes', True)
        check_type_dep(ctype.return_type)
        for arg in ctype.argument_types:
            check_type_dep(arg)
        module.flush_dep()
        module.code.append(
            '%s = %s(%s)' % (
                ctype.name,
                ctype.constructor,
                ', '.join([ctype.return_type.to_source()] + [arg.to_source() for arg in ctype.argument_types])
            )
        )
        is_callback = f'PFN_{name}' in context.callback_map
        if is_callback:
            code.append('%s.__doc__ = %r' % (name, 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/PFN_%s.html' % name))
        else:
            code.append('%s.__doc__ = %r' % (name, 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/%s.html' % name))
        code.append('%s._vulkan_type_ = %s' % (ctype.name, ctype.get_runtime_source()))
        code.append('%s._vulkan_type_._class_ = %s' % (ctype.name, ctype.name))
        if is_callback:
            code.append('%s._vulkan_callback_ = %r' % (name, f'PFN_{name}'))
        return code

    
    def _write_vulkan_database(self, context: Context):
        module = GeneratedModule(['_vulkan_database'])
        module.lines.append('vendor_suffix = [')
        for name in sorted(context.tag_set):
            module.lines.append('    %r,' % name)
        module.lines.append(']')
        module.lines.append('')
        module.update_file(self.base_dir)

    def _write_vulkan_enum(self, context: Context, enum_name: str):
        module = GeneratedModule(['_vulkan_enum', enum_name])
        descriptor = context.enum_map[enum_name]
        type_descriptor = context.plain_ctype_class[descriptor['class']][descriptor['ctype'].ctype()]
        module.lines.extend(['from enum import %s' % type_descriptor['base_class_name'], ''])
        module.lines.append('class %s(%s):' % (enum_name, type_descriptor['base_class_name']))
        values = {}
        for value_name in descriptor['values']:
            value_descriptor = context.value_map[value_name]
            values[value_name] = '    %s = %r' % (value_name, value_descriptor['value'])
        if len(values) > 0:
            for value_name in sorted(values.keys()):
                module.lines.append(values[value_name])
            alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if value in values}
            for name in sorted(alias.keys()):
                value = alias[name]
                module.lines.append('    %s = %s' % (name, value))
        else:
            module.lines.append('    pass')
        module.lines.append('')
        module.lines.append('%s.__doc__ = %r' % (enum_name, 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/%s.html' % enum_name))
        module.lines.append('')
        module.update_file(self.base_dir)

    def _write_vulkan_enums(self, context: Context):
        if len(context.enum_map) <= 0:
            return
        module = GeneratedModule(['_vulkan_enum', '__init__'])
        for enum_name in context.enum_map:
            module.add_dep(f'.{enum_name}', enum_name)
        module.lines.append('')
        alias_enum = { k: v for k, v in context.alias_map.items() if v in context.enum_map }
        for alias_name in sorted(alias_enum.keys()):
            enum_name = alias_enum[alias_name]
            module.lines.append('%s = %s' % (alias_name, enum_name))
        module.lines.append('')
        module.update_file()

    def _write_vulkan_value(self, context: Context):
        module = GeneratedModule('_vulkan_value')
        code = ['import ctypes']
        enum_set = set()
        exports = set()
        for descriptor in context.value_map.values():
            if 'enum_name' in descriptor:
                enum_set.add(descriptor['enum_name'])
        for enum_name in sorted(enum_set):
            code.append('from ._vulkan_enum.%s import %s' % (enum_name, enum_name))
        code.append('')
        value_map = {}
        for name, descriptor in context.value_map.items():
            exports.add(name)
            if 'enum_name' in descriptor:
                value_map[name] = '%s = %s.%s' % (name, descriptor['enum_name'], name)
            else:
                value_map[name] = '%s = %r' % (name, descriptor['value'])
        for name in sorted(value_map.keys()):
            code.append(value_map[name])
        code.append('')
        for name in sorted(context.object_macro_map.keys()):
            exports.add(name)
            descriptor = context.object_macro_map[name]
            code.append('%s = %r' % (name, descriptor['value']))
        code.append('')
        for name in sorted([k for k, v in context.func_macro_map.items() if 'python_node' in v]):
            exports.add(name)
            descriptor = context.func_macro_map[name]
            func_code = ast.unparse(descriptor['python_node']).split(linesep)
            func_code.append('')
            code.extend(func_code)
        alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if value in context.value_map}
        for name in sorted(alias.keys()):
            exports.add(name)
            code.append('%s = %s' % (name, alias[name]))
        code.append('__all__ = [')
        for name in sorted(exports):
            code.append('    %r,' % name)
        code.extend([']', ''])
        file = self.base_dir.joinpath('_vulkan_value.py')
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_callback(self, context: Context, name: str):
        module = GeneratedModule()
        self._create_function_source(context, name, module)
        info = context.callback_map[f'PFN_{name}']
        code.append('%s._vulkan_type_.return_type = %s' % (name, info['return'].get_runtime_source()))
        for arg_index, arg_name in enumerate(info['arg_list']):
            arg_type = info['arg_map'][arg_name]
            info['node'].children['type'][arg_index]
            code.append('%s._vulkan_ctype_.arguments[%r] = %s' % (name, arg_name, arg_type.get_runtime_source()))
        code.append('')
        file = self.base_dir.joinpath('_vulkan_callback/%s.py' % name)
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))
    
    def _write_vulkan_callbacks(self, context: Context):
        code = []
        for name in [context.ctypes_map[k].name for k in context.type_node_map['funcpointer'].keys()]:
            self._write_vulkan_callback(context, name)
            code.append('from .%s import %s' % (name, name))
        code.append('')

        file = self.base_dir.joinpath('_vulkan_callback/__init__.py')
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))
    
    def _write_vulkan_type(self, context: Context, name: str):
        code = ['import ctypes', 'from ..._ctypes import *', '']
        ctype = context.ctypes_map[name]
        ctype: CComplexType
        info = context.struct_map[name]

        def generate_class_body():
            return False

        code.append('class %s(ctypes.%s):' % (name, ctype.constructor))
        member_types = [ctype.member_map[x]['node'].get('type').get_text() for x in ctype.member_list]
        complex_member_types = set([x for x in member_types if x in context.type_node_map['complex']])
        funcpointer_member_types = set([x for x in member_types if x in context.type_node_map['funcpointer']])
        delay_fields = ctype['delay_fields'] or name in complex_member_types or name in funcpointer_member_types
        in_class_body = True
        if delay_fields or len(complex_member_types) > 0 or len(funcpointer_member_types) > 0:
            if not generate_class_body():
                code.append('    pass')
            in_class_body = False
            code.append('')
            for dependency in sorted([context.ctypes_map[t].name for t in funcpointer_member_types]):
                code.append('from .._vulkan_callback.%s import %s' % (dependency, dependency))
            for dependency in sorted(complex_member_types):
                if dependency != name:
                    code.append('from .%s import %s' % (dependency, dependency))
            code.append('')
            code.append('%s._fields_ = [' % name)
            indent = 1
        else:
            code.append('    _fields_ = [')
            indent = 2
        for member_name in ctype.member_list:
            member_desc = ctype.member_map[member_name]
            if 'bitsize' in member_desc:
                code.append('%s(%r, %s, %d),' % ('    ' * indent, member_name, member_desc['ctype'].to_source(), member_desc['bitsize']))
            else:
                code.append('%s(%r, %s),' % ('    ' * indent, member_name, member_desc['ctype'].to_source()))
        code.append('    ' * (indent - 1) + ']')
        code.append('')
        code.append('%s.__doc__ = %r' % (name, 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/%s.html' % name))
        code.append('')
        if in_class_body:
            generate_class_body()
        members = OrderedDict()
        member_deps = {
            'enum': set(),
            'value': set()
        }
        for member_name in ctype.member_list:
            member_info = ctype.member_map[member_name]
            member_code = ['    %r: {' % member_name]
            member_type = member_info['node'].get('type').get_text()
            member_type_class = 'ctypes'
            if member_type in context.enum_map:
                member_type_class = 'enum'
                member_deps['enum'].add(member_type)
                member_code.append('        %r: %s,' % ('enum', member_type))
            elif member_type in context.type_node_map['complex']:
                member_type_class = context.ctypes_map[member_type].constructor.lower()
            elif member_type in context.type_node_map['funcpointer']:
                member_type_class = 'callback'
            elif member_type in context.type_node_map['handle']:
                member_type_class = 'handle'
            member_code.append('        %r: %r,' % ('type', {
                'class': member_type_class,
                'name': member_type
            }))
            if member_info['node'].has_attribute('values'):
                member_value = member_info['node'].attributes['values']
                if member_value in context.value_map:
                    member_deps['value'].add(member_value)
                    member_code.append('        %r: %s,' % ('value', member_value))
            members[member_name] = member_code
            if member_info['node'].has_attribute('selection'):
                assert ctype.constructor == 'Union'
                member_selection = member_info['node'].attributes['selection']
                if member_selection in context.value_map:
                    member_deps['value'].add(member_selection)
                    member_code.append('        %r: %s,' % ('selection', member_selection))
            if member_info['node'].has_attribute('selector'):
                member_selector = member_info['node'].attributes['selector']
                assert member_selector in ctype.member_list
                member_code.append('        %r: %r,' % ('selector', member_selector))
            if member_info['node'].has_attribute('len'):
                member_len = member_info['node'].attributes['len']
                if member_len.startswith('latexmath:'):
                    assert member_info['node'].has_attribute('altlen')
                    member_len = member_info['node'].attributes['altlen']
                member_len = [x.replace('->', '.') for x in member_len.split(',')]
                member_code.append('        %r: %r,' % ('length', member_len))
            member_externsync = False
            if member_info['node'].has_attribute('externsync'):
                assert member_info['node'].attributes['externsync'].lower() == 'true'
                member_externsync = True
            member_code.append('        %r: %r,' % ('sync', member_externsync))
            if member_info['node'].has_attribute('objecttype'):
                # This should be only applied to uint64_t type.
                # The field specified in objecttype specify type of handle, while the uint64_t specify the value of the handle, if any.
                member_objecttype = member_info['node'].attributes['objecttype']
                assert member_objecttype in ctype.member_list
                member_code.append('        %r: %r,' % ('handle_type', member_objecttype))
            if member_info['node'].has_attribute('limittype'):
                member_limittype = member_info['node'].attributes['limittype']
                member_code.append('        %r: %r,' % ('limit_function', member_limittype))
            member_code.append('    },')
            members[member_name] = member_code

        if len(member_deps['enum']) > 0 or len(member_deps['value']) > 0:
            code.append('')
            if len(member_deps['enum']) > 0:
                code.append('from .._vulkan_enum import %s' % ', '.join(sorted(member_deps['enum'])))
            if len(member_deps['value']) > 0:
                code.append('from .._vulkan_value import %s' % ', '.join(sorted(member_deps['value'])))
        code.append('')

        code.append('%s._vulkan_ctype_ = %s' % (name, ctype.get_runtime_source()))
        code.append('%s._vulkan_ctype_._class_ = %s' % (name, name))
        for member_name in ctype.member_list:
            code.append('%s._vulkan_ctype_.fields[%r] = %s' % (
                name,
                member_name,
                ctype.member_map[member_name]['ctype'].get_runtime_source()
            ))

        code.append('%s._vulkan_fields_ = {' % name)
        for member_code in members.values():
            code.extend(member_code)
        code.append('}')
        code.append('')

        file = self.base_dir.joinpath('_vulkan_type/%s.py' % (name))
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_types(self, context: Context):
        code = []
        deps = []
        for name in context.type_node_map['complex']:
            self._write_vulkan_type(context, name)
            deps.append(name)
        for name in sorted(deps):
            code.append('from .%s import %s' % (name, name))
        alias_map = { k: v for k, v in context.alias_map.items() if v in context.type_node_map['complex'] }
        for alias_name in sorted(alias_map.keys()):
            type_name = alias_map[alias_name]
            code.append('%s = %s' % (alias_name, type_name))
        file = self.base_dir.joinpath('_vulkan_type/__init__.py')
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_handles(self, context: Context):
        code = ['from .._ctypes import *', '']
        for handle_name in context.handle_map:
            handle_info = context.handle_map[handle_name]
            code.append('%s = %s' % (handle_name, handle_info['ctype'].get_runtime_source()))
        code.append('')
        for handle_name in context.handle_map:
            handle_info = context.handle_map[handle_name]
            is_dispatchable = handle_info['typedef'] != 'VK_DEFINE_NON_DISPATCHABLE_HANDLE'
            code.append('%s.dispatchable = %r' % (handle_name, is_dispatchable))
            if 'parent' in handle_info and isinstance(handle_info['parent'], str):
                code.append('%s.parent = %s' % (handle_name, handle_info['parent']))
        code.append('')

        handle_alias = { k: v for k, v in context.alias_map.items() if v in context.handle_map }
        for alias_name, handle_name in handle_alias.items():
            code.append('%s = %s' % (alias_name, handle_name))
        code.append('')
        
        file = self.base_dir.joinpath('_vulkan_handle.py')
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_command(self, context: Context, name: str):
        ctype = context.ctypes_map[name]
        info = context.command_map[name]
        dep_map = { 'enum': set() }
        code = ['import ctypes', 'from collections import OrderedDict', 'from ..._ctypes import *']
        fn_code = self._create_function_source(context, name, dep_map)
        for arg_name in info['argument_list']:
            arg_info = info['argument_map'][arg_name]
            arg_type = arg_info['type']
            if arg_type in context.enum_map:
                dep_map['enum'].add(arg_type)
            if arg_info['node'].has_attribute('validstructs'):
                arg_valid_struct_list = [x.strip() for x in arg_info['node'].get_attribute('validstructs').split(',')]
                for arg_struct in arg_valid_struct_list:
                    arg_struct = context.resolve_alias(arg_struct)
                    assert arg_struct in context.type_node_map['complex'] and arg_struct in context.ctypes_map
                    assert tuple(context.ctypes_map[arg_struct].member_list[:2]) == ('sType', 'pNext')
                    dep_map['struct'].add(arg_struct)
        if 'struct' in dep_map and len(dep_map['struct']) > 0:
            for dep_name in sorted(dep_map['struct']):
                code.append('from .._vulkan_type.%s import %s' % (dep_name, dep_name))
        if 'callback' in dep_map and len(dep_map['callback']) > 0:
            for dep_name in sorted(dep_map['callback']):
                code.append('from .._vulkan_callback.%s import %s' % (dep_name, dep_name))
        if 'enum' in dep_map and len(dep_map['enum']) > 0:
            for dep_name in sorted(dep_map['enum']):
                code.append('from .._vulkan_enum.%s import %s' % (dep_name, dep_name))
        code.append('')
        return_status = info['return']['type'] == 'VkResult'
        if return_status:
            code.append('from .._vulkan_enum.VkResult import VkResult')
        code.extend(fn_code)
        code.append('%s.__doc__ = %r' % (name, 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/%s.html' % name))
        code.append('%s._vulkan_ctype_.return_type = %s' % (name, info['return']['ctype'].get_runtime_source()))
        for arg_name in info['argument_list']:
            arg_type = info['argument_map'][arg_name]['ctype']
            code.append('%s._vulkan_ctype_.arguments[%r] = %s' % (name, arg_name, arg_type.get_runtime_source()))
        code.append('')
        if return_status or info['return']['type'] == 'void':
            return_arguments = [arg_name for arg_name in info['argument_list'] if info['argument_map'][arg_name]['output']]
        else:
            return_arguments = []
        code.append('%s._vulkan_return_ = {' % name)
        code.append('    %r: %r,' % ('status', return_status))
        code.append('    %r: %r,' % ('arguments', return_arguments))
        if return_status:
            if 'success_code_list' in info:
                code.append('    %r: [%s],' % ('success', ', '.join(f'VkResult.{x}' for x in sorted(info['success_code_list']))))
            else:
                code.append('    %r: [],' % ('success'))
            if 'error_code_list' in info:
                code.append('    %r: [%s],' % ('error', ', '.join(f'VkResult.{x}' for x in sorted(info['error_code_list']))))
            else:
                code.append('    %r: [],' % ('error'))
        code.append('}')
        code.append('%s._vulkan_arguments_ = OrderedDict()' % name)
        externsync = []
        for arg_name in info['argument_list']:
            arg_code = []
            arg_info = info['argument_map'][arg_name]
            code.append('%s._vulkan_arguments_[%r] = {' % (name, arg_name))
            arg_type = arg_info['type']
            arg_type_class = 'ctypes'
            if arg_type in context.enum_map:
                arg_type_class = 'enum'
                arg_code.append('    %r: %s,' % ('enum', arg_type))
            elif arg_type in context.type_node_map['complex']:
                arg_type_class = context.ctypes_map[arg_type].constructor.lower()
            elif arg_type in context.type_node_map['funcpointer']:
                arg_type_class = 'callback'
            elif arg_type in context.type_node_map['handle']:
                arg_type_class = 'handle'
            code.append('    %r: %r,' % ('type', {
                'class': arg_type_class,
                'name': arg_type
            }))
            code.extend(arg_code)
            arg_optional = []
            if arg_info['node'].has_attribute('optional'):
                arg_optional = [x.strip().lower() == 'true' for x in arg_info['node'].get_attribute('optional').split(',')]
            if len(arg_optional) == 0:
                arg_optional.append(False)
            code.append('    %r: %r,' % ('optional', arg_optional))
            if arg_info['node'].has_attribute('externsync'):
                arg_externsync = arg_info['node'].get_attribute('externsync')
                if arg_externsync == 'true':
                    externsync.append(arg_name)
                else:
                    arg_externsync = [x.strip().replace('[]', '[:]').replace('->', '.') for x in arg_externsync.split(',')]
                    externsync.extend(arg_externsync)
            if arg_info['node'].has_attribute('len'):
                length = arg_info['node'].get_attribute('len')
                if arg_info['node'].has_attribute('altlen'):
                    length = arg_info['node'].get_attribute('altlen')
                length = [item.strip().replace('[]', '[:]').replace('->', '.') for item in length.split(',')]
                code.append('    %r: %r,' % ('length', length))
            if arg_info['node'].has_attribute('selector'):
                # Note: currently no command takes union argument, thus no command contain @selector attribute
                arg_selector = arg_info['node'].get_attribute('selector')
                code.append('    %r: %r,' % ('selector', arg_selector.strip().replace('->', '.')))
            if arg_info['node'].has_attribute('objecttype'):
                # Indicator that the current 64-bit integer type contains a handle. Its content will be the name
                # of another argument (or argument's struct member) that contain enumeration specifying the type
                # of the contained handle. The handle can be NULL, in which case the type does not matter.
                arg_objecttype = arg_info['node'].get_attribute('objecttype')
                code.append('    %r: %r,' % ('handle_type', arg_objecttype.strip().replace('->', '.')))
            if arg_info['node'].has_attribute('validstructs'):
                # In some cases the argument is an I/O of generic VkBaseInStructure or VkBaseOutStructure.
                # In such case the argument should point to one or more structures chained with pNext and determined by sType.
                # Which type of structures are supported for this parameter will be determined by the @validstructs
                arg_valid_struct_list = [x.strip() for x in arg_info['node'].get_attribute('validstructs').split(',')]
                arg_struct_set = set()
                for arg_struct in arg_valid_struct_list:
                    arg_struct = context.resolve_alias(arg_struct)
                    arg_struct_set.add(arg_struct)
                code.append('    %r: {%r},' % ('structure_type', ', '.join(sorted(arg_struct_set))))
            code.append('}')
        if len(externsync) > 0:
            code.append('%s._vulkan_sync_ = [' % name)
            for sname in externsync:
                code.append('    %r,' % sname)
            code.append(']')
        else:
            code.append('%s._vulkan_sync_ = []' % name)
        doc_text = []
        if 'implicitexternsyncparams' in info['node'].children:
            for sync_doc in info['node'].get_all('implicitexternsyncparams'):
                for sync_doc_param in sync_doc.get_all('param'):
                    sync_doc_param_text = sync_doc_param.get_text().strip()
                    if len(sync_doc_param_text) > 0:
                        doc_text.append(sync_doc_param_text)
        if len(doc_text) > 0:
            code.append('%s._vulkan_sync_doc_ = [' % name)
            for doc_entry in doc_text:
                code.append('    %r,' % doc_entry)
            code.append(']')
        else:
            code.append('%s._vulkan_sync_doc_ = []' % name)
        code.append('')

        file = self.base_dir.joinpath('_vulkan_command/%s.py' % (name))
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))


    def _write_vulkan_commands(self, context: Context):
        code = []
        for name in context.command_map:
            self._write_vulkan_command(context, name)
            code.append('from .%s import %s' % (name, name))
        alias_map = { k: v for k, v in context.alias_map.items() if v in context.command_map }
        for alias_name in sorted(alias_map.keys()):
            name = alias_map[alias_name]
            code.append('%s = %s' % (alias_name, name))
        code.append('')

        file = self.base_dir.joinpath('_vulkan_command/__init__.py')
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def generate(self, context: Context):
        self.base_dir.mkdir(mode = 0o755, parents = True, exist_ok = True)
        self._write_vulkan_database(context)
        self._write_vulkan_enums(context)
        self._write_vulkan_value(context)
        self._write_vulkan_callbacks(context)
        self._write_vulkan_types(context)
        self._write_vulkan_handles(context)
        self._write_vulkan_commands(context)
