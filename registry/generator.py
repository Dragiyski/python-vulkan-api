import ctypes
import ast
import pycparser.c_ast
from collections import OrderedDict
from pathlib import Path
from .context import Context
from .platform import CType, CPointerType, CArrayType, CComplexType, CFunctionType
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
        self.slots = OrderedDict([
            ('import', []),
            ('main', []),
        ])
        self.deps = {
            'import': {}
        }
        self.default_slot = 'main'
        self.default_import_slot = 'import'
        self.current_indent = 0
        self.started_line = None

    def add_dep(self, module: str, selector: str | bool, *, slot=None):
        if slot is None:
            slot = self.default_import_slot
        if slot not in self.deps:
            raise RuntimeError(f'Slot "{slot}" already flushed')
        if module not in self.deps[slot]:
            self.deps[slot][module] = {}
        if selector not in self.deps[slot][module]:
            self.deps[slot][module][selector] = False

    def add_slot(self, name: str, is_import: bool = False):
        if name in self.slots:
            raise RuntimeError(f'Slot "{name}" already exists')
        self.slots[name] = []
        if is_import:
            self.deps[name] = {}

    def flush_dep(self, slot=None):
        if slot is None:
            slot = self.default_import_slot
        if self.deps[slot] is None:
            return
        has_import = False
        for mod in module_sorted(self.deps[slot].keys()):
            ns = self.deps[slot][mod]
            if False in ns and not ns[False]:
                self.append_lines('import %s' % mod, slot=slot)
                has_import = True
                ns[False] = True
            if True in ns and not ns[True]:
                self.append_lines('from %s import *' % mod, slot=slot)
                has_import = True
                ns[True] = True
            names = {k: v for k, v in ns.items() if isinstance(k, str) and not v}
            if len(names) > 3:
                has_import = True
                self.append_lines('from %s import (' % mod, slot=slot)
                for name in sorted(names):
                    self.append_lines('    %s,' % name, slot=slot)
                    ns[name] = True
                self.append_lines(')', slot=slot)
            elif len(names) > 0:
                self.append_lines('from %s import %s' % (mod, ', '.join(sorted(names.keys()))), slot=slot)
                has_import = True
                for name in names:
                    ns[name] = True
        if has_import:
            self.append_lines('', slot=slot)
        self.deps[slot] = None

    def append_lines(self, *lines: str, slot=None):
        if slot is None:
            slot = self.default_slot
        for line in lines:
            if self.started_line is not None:
                line = self.started_line + line
                self.started_line = None
            self.slots[slot].append((('    ' * self.current_indent) + line + linesep) if line.strip() else linesep)

    def update_file(self, base_path: Path):
        for slot in self.deps:
            self.flush_dep(slot)
        path = base_path.joinpath('/'.join(self.path) + '.py')
        path.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
        with open(path, 'w') as stream:
            for slot in self.slots:
                stream.writelines(self.slots[slot])


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
        if ctype.constructor in ['VKAPI_CALL', 'VKAPI_PTR']:
            module.add_dep('..._vk_base', ctype.constructor)
        check_type_dep(ctype.return_type)
        for arg in ctype.argument_types:
            check_type_dep(arg)
        module.append_lines(
            '%s = %s(%s)' % (
                ctype.name,
                ctype.constructor,
                ', '.join([ctype.return_type.to_source()] + [arg.to_source() for arg in ctype.argument_types])
            )
        )
        is_callback = f'PFN_{name}' in context.callback_map
        if is_callback:
            module.append_lines('%s.__doc__ = %r' % (name, 'https://docs.vulkan.org/refpages/latest/refpages/source/PFN_%s.html' % name))
        else:
            module.append_lines('%s.__doc__ = %r' % (name, 'https://docs.vulkan.org/refpages/latest/refpages/source/%s.html' % name))

    def _write_vulkan_database(self, context: Context):
        module = GeneratedModule(['_vulkan_database'])
        module.append_lines('vendor_suffix = [')
        module.current_indent += 1
        for name in sorted(context.tag_set):
            module.append_lines('%r,' % name)
        module.current_indent -= 1
        module.append_lines(']', '')
        module.update_file(self.base_dir)

    def _write_vulkan_enum(self, context: Context, enum_name: str):
        module = GeneratedModule(['_vulkan_enum', enum_name])
        descriptor = context.enum_map[enum_name]
        type_descriptor = context.plain_ctype_class[descriptor['class']][descriptor['ctype'].ctype()]
        module.add_dep('ctypes', False)
        module.add_dep('enum', type_descriptor['base_class_name'])
        module.append_lines('class %s(%s):' % (enum_name, type_descriptor['base_class_name']))
        values = {}
        for value_name in descriptor['values']:
            value_descriptor = context.value_map[value_name]
            values[value_name] = '    %s = %r' % (value_name, value_descriptor['value'])
        if len(values) > 0:
            for value_name in sorted(values.keys()):
                module.append_lines(values[value_name])
            alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if value in values}
            for name in sorted(alias.keys()):
                value = alias[name]
                module.append_lines('    %s = %s' % (name, value))
        else:
            module.append_lines('    pass')
        module.append_lines('', '%s.__doc__ = %r' % (enum_name, 'https://docs.vulkan.org/refpages/latest/refpages/source/%s.html' % enum_name))
        module.append_lines('%s._vulkan_ = {' % enum_name)
        module.append_lines('    %r: %s,' % ('ctype', descriptor['ctype'].to_source()))
        module.append_lines('    %r: %r,' % ('class', descriptor['class']))
        module.append_lines('}')
        module.update_file(self.base_dir)

    def _write_vulkan_enums(self, context: Context):
        if len(context.enum_map) <= 0:
            return
        module = GeneratedModule(['_vulkan_enum', '__init__'])
        for enum_name in context.enum_map:
            self._write_vulkan_enum(context, enum_name)
            module.add_dep(f'.{enum_name}', enum_name)
        alias_enum = {k: v for k, v in context.alias_map.items() if v in context.enum_map}
        for alias_name in sorted(alias_enum.keys()):
            enum_name = alias_enum[alias_name]
            module.append_lines('%s = %s' % (alias_name, enum_name))
        module.update_file(self.base_dir)

    def _write_vulkan_value(self, context: Context):
        module = GeneratedModule(['_vulkan_value'])
        module.add_dep('ctypes', False)
        enum_set = set()
        exports = set()
        for descriptor in context.value_map.values():
            if 'enum_name' in descriptor:
                enum_set.add(descriptor['enum_name'])
        for enum_name in sorted(enum_set):
            module.add_dep('._vulkan_enum.%s' % enum_name, enum_name)
        value_map = {}
        for name, descriptor in context.value_map.items():
            exports.add(name)
            if 'enum_name' in descriptor:
                value_map[name] = '%s = %s.%s' % (name, descriptor['enum_name'], name)
            else:
                value_map[name] = '%s = %r' % (name, descriptor['value'])
        for name in sorted(value_map.keys()):
            module.append_lines(value_map[name])
        module.append_lines('')
        for name in sorted(context.object_macro_map.keys()):
            exports.add(name)
            descriptor = context.object_macro_map[name]
            module.append_lines('%s = %r' % (name, descriptor['value']))
        module.append_lines('')
        for name in sorted([k for k, v in context.func_macro_map.items() if 'python_node' in v]):
            exports.add(name)
            descriptor = context.func_macro_map[name]
            func_code = ast.unparse(descriptor['python_node']).split(linesep)
            module.append_lines(*func_code, '')
        alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if value in context.value_map}
        for name in sorted(alias.keys()):
            exports.add(name)
            module.append_lines('%s = %s' % (name, alias[name]))
        module.append_lines('__all__ = [')
        for name in sorted(exports):
            module.append_lines('    %r,' % name)
        module.append_lines(']')
        module.update_file(self.base_dir)

    def _write_vulkan_callback(self, context: Context, name: str):
        module = GeneratedModule(['_vulkan_callback', name])
        module.add_dep('ctypes', False)
        module.add_dep('collections', 'OrderedDict')
        self._create_function_source(context, name, module)
        info = context.callback_map[f'PFN_{name}']
        module.append_lines('')
        module.append_lines('%s._vulkan_ = {' % name)
        module.current_indent += 1
        module.append_lines('%r: {' % ('return'))
        module.current_indent += 1
        module.append_lines('%r: %r,' % ('type', info['return']['type']))
        module.append_lines('%r: %s,' % ('ctype', info['return']['ctype'].to_source()))
        module.append_lines('%r: %r,' % ('class', self._get_type_class(context, info['return']['type'])))
        module.current_indent -= 1
        module.append_lines('},')
        module.append_lines('%r: OrderedDict([' % ('arguments'))
        module.current_indent += 1
        for arg_name in info['argument_list']:
            arg_info = info['argument_map'][arg_name]
            module.append_lines('(')
            module.current_indent += 1
            module.append_lines('%r,' % arg_name)
            module.append_lines('{')
            module.current_indent += 1
            module.append_lines('%r: %r,' % ('type', arg_info['type']))
            module.append_lines('%r: %s,' % ('ctype', arg_info['ctype'].to_source()))
            module.append_lines('%r: %r,' % ('class', self._get_type_class(context, arg_info['type'])))
            if 'cdecl' in arg_info:
                module.started_line = '%r: ' % ('cdecl')
                self._write_cdecl_source(context, module, arg_info['cdecl'])
            for attribute_name in arg_info['node'].attributes:
                module.append_lines('%r: %r,' % (f'@{attribute_name}', arg_info['node'].get_attribute(attribute_name)))
            module.append_lines('%r: %r,' % ('python_name', context.make_python_name(arg_name, skip_prefixes=('p', 'pp', 's'))))
            module.current_indent -= 1
            module.append_lines('},')
            module.current_indent -= 1
            module.append_lines('),')
        module.current_indent -= 1
        module.append_lines(']),')
        for attribute_name in info['node'].attributes:
            module.append_lines('%r: %r,' % (f'@{attribute_name}', info['node'].get_attribute(attribute_name)))
        module.current_indent -= 1
        module.append_lines('}')
        module.append_lines('')

        module.update_file(self.base_dir)

    def _write_vulkan_callbacks(self, context: Context):
        module = GeneratedModule(['_vulkan_callback', '__init__'])
        for name in [context.ctypes_map[k].name for k in context.type_node_map['funcpointer'].keys()]:
            self._write_vulkan_callback(context, name)
            module.add_dep('.%s' % name, name)
        module.update_file(self.base_dir)

    def _write_vulkan_type(self, context: Context, name: str):
        module = GeneratedModule(['_vulkan_type', name])
        module.add_dep('ctypes', False)
        ctype = context.ctypes_map[name]
        ctype: CComplexType
        info = context.struct_map[name]
        member_types = [ctype.member_map[x]['node'].get('type').get_text() for x in ctype.member_list]
        complex_member_types = set([x for x in member_types if x in context.type_node_map['complex']])
        funcpointer_member_types = set([x for x in member_types if x in context.type_node_map['funcpointer']])
        delay_fields = ctype['delay_fields'] or name in complex_member_types or name in funcpointer_member_types
        delay_fields = delay_fields or len(complex_member_types) > 0 or len(funcpointer_member_types) > 0

        module.add_dep('ctypes', False)
        module.add_dep('collections', 'OrderedDict')

        module.append_lines('class %s(ctypes.%s):' % (name, ctype.constructor))
        if delay_fields:
            module.append_lines('    pass', '')
            module.add_slot('fields_import', is_import=True)
            module.add_slot('fields')
            module.default_import_slot = 'fields_import'
            module.default_slot = 'fields'
        else:
            module.current_indent += 1

        for dependency in sorted([context.ctypes_map[t].name for t in funcpointer_member_types]):
            module.add_dep('.._vulkan_callback.%s' % dependency, dependency)
        for dependency in sorted(complex_member_types):
            if dependency != name:
                module.add_dep('.%s' % dependency, dependency)

        module.append_lines(
            '%s._fields_ = [' % name
            if delay_fields
            else '_fields_ = ['
        )
        module.current_indent += 1
        for member_name in ctype.member_list:
            member_desc = ctype.member_map[member_name]
            if 'bitsize' in member_desc:
                module.append_lines('(%r, %s, %d),' % (member_name, member_desc['ctype'].to_source(), member_desc['bitsize']))
            else:
                module.append_lines('(%r, %s),' % (member_name, member_desc['ctype'].to_source()))
        module.current_indent -= 1
        module.append_lines(']')
        while module.current_indent > 0:
            module.current_indent -= 1
        module.append_lines('')
        module.add_slot('metadata')
        module.default_slot = 'metadata'
        module.append_lines('%s.__doc__ = %r' % (name, 'https://docs.vulkan.org/refpages/latest/refpages/source/%s.html' % name))
        module.append_lines('%s._vulkan_ = {' % name)
        module.current_indent += 1
        is_extensible_struct = False
        is_output = True
        if (
            'sType' in info['ctype'].member_map
            and
            'pNext' in info['ctype'].member_map
            and
            info['ctype'].member_map['sType']['type'] == 'VkStructureType'
            and
            info['ctype'].member_map['sType']['node'].has_attribute('values')
        ):
            is_extensible_struct = True
            if 'const' in info['ctype'].member_map['pNext']['cdecl'].quals:
                is_output = False
        hidden_fields = set()
        if is_extensible_struct:
            hidden_fields.update(['sType', 'pNext'])
            module.add_dep('.._vulkan_enum.VkStructureType', 'VkStructureType')
            module.append_lines('%r: VkStructureType.%s,' % ('structure_type', info['ctype'].member_map['sType']['node'].get_attribute('values')))
            if info['node'].has_attribute('structextends'):
                struct_extends = info['node'].attributes['structextends'].split(',')
                if len(struct_extends) > 0:
                    module.append_lines('%r: [' % ('struct_extends'))
                    module.current_indent += 1
                    for struct_extend in struct_extends:
                        module.add_dep('.%s' % struct_extend, struct_extend)
                        module.append_lines(struct_extend + ',')
                    module.current_indent -= 1
                    module.append_lines('],')
                else:
                    module.append_lines('%r: [],' % ('struct_extends'))
        module.append_lines('%r: %r,' % ('is_extensible_struct', is_extensible_struct))
        module.append_lines('%r: %r,' % ('is_output', is_output))
        for attribute_name in info['node'].attributes:
            module.append_lines('%r: %r,' % (f'@{attribute_name}', info['node'].get_attribute(attribute_name)))
        module.append_lines('%r: OrderedDict([' % ('members'))
        module.current_indent += 1
        for member_name in ctype.member_list:
            module.append_lines('(')
            module.current_indent += 1
            member_info = ctype.member_map[member_name]
            module.append_lines('%r,' % member_name)
            module.append_lines('{')
            module.current_indent += 1
            if 'type' in member_info:
                module.append_lines('%r: %r,' % ('type', member_info['type']))
                module.append_lines('%r: %r,' % ('class', self._get_type_class(context, member_info['type'])))
            elif 'type' in member_info['node'].children:
                member_type = member_info['node'].get('type').get_text()
                if member_type not in context.ctypes_map or context.ctypes_map[member_type].__class__ == CType:
                    module.append_lines('%r: %r,' % ('type', member_type))
                    module.append_lines('%r: %r,' % ('class', 'external'))
                else:
                    module.append_lines('%r: %r,' % ('type', member_type))
                    module.append_lines('%r: %r,' % ('class', 'ctypes'))
            else:
                module.append_lines('%r: %r,' % ('class', 'ctypes'))
            module.append_lines('%r: %s,' % ('ctype', member_info['ctype'].to_source()))
            if member_name not in hidden_fields:
                module.append_lines('%r: %r,' % ('python_name', context.make_python_name(member_name, skip_prefixes=('p', 'pp', 's'))))
            member_node = member_info['node']
            if 'cdecl' in member_info:
                module.started_line = '%r: ' % ('cdecl')
                self._write_cdecl_source(context, module, member_info['cdecl'])
            for attribute_name in member_node.attributes:
                module.append_lines('%r: %r,' % (f'@{attribute_name}', member_node.get_attribute(attribute_name)))
            module.current_indent -= 1
            module.append_lines('},')
            module.current_indent -= 1
            module.append_lines('),')
        module.current_indent -= 1
        module.append_lines('])')
        module.current_indent -= 1
        module.append_lines('}')

        module.update_file(self.base_dir)

    def _write_vulkan_types(self, context: Context):
        module = GeneratedModule(['_vulkan_type', '__init__'])
        for name in context.type_node_map['complex']:
            self._write_vulkan_type(context, name)
            module.add_dep('.%s' % name, name)
        alias_map = {k: v for k, v in context.alias_map.items() if v in context.type_node_map['complex']}
        for alias_name in sorted(alias_map.keys()):
            type_name = alias_map[alias_name]
            module.append_lines('%s = %s' % (alias_name, type_name))

        module.update_file(self.base_dir)

    def _write_vulkan_handles(self, context: Context):
        module = GeneratedModule(['_vulkan_handle'])
        module.add_dep('ctypes', False)
        module.add_dep('.._vk_base', 'VK_DEFINE_HANDLE')
        module.add_dep('.._vk_base', 'VK_DEFINE_NON_DISPATCHABLE_HANDLE')
        for handle_name in context.handle_map:
            handle_info = context.handle_map[handle_name]
            module.append_lines('%s = %s' % (handle_name, handle_info['ctype'].get_runtime_source()))
        module.append_lines('')
        for handle_name in context.handle_map:
            handle_info = context.handle_map[handle_name]
            is_dispatchable = handle_info['typedef'] != 'VK_DEFINE_NON_DISPATCHABLE_HANDLE'
            module.append_lines('%s.dispatchable = %r' % (handle_name, is_dispatchable))
            if 'parent' in handle_info and isinstance(handle_info['parent'], str):
                module.append_lines('%s.parent = %s' % (handle_name, handle_info['parent']))
        module.append_lines('')

        handle_alias = {k: v for k, v in context.alias_map.items() if v in context.handle_map}
        for alias_name, handle_name in handle_alias.items():
            module.append_lines('%s = %s' % (alias_name, handle_name))
        module.append_lines('')

        module.update_file(self.base_dir)

    def _get_type_class(self, context: Context, type_name: str):
        type_class = 'ctypes'
        if type_name in context.enum_map:
            type_class = 'enum'
        elif type_name in context.type_node_map['complex']:
            type_class = 'type'
        elif type_name in context.type_node_map['funcpointer']:
            type_class = 'callback'
        elif type_name in context.type_node_map['handle']:
            type_class = 'handle'
        return type_class

    def _write_vulkan_command(self, context: Context, name: str):
        module = GeneratedModule(['_vulkan_command', name])
        info = context.command_map[name]
        dep_map = {'enum': set(), 'struct': set(), 'callback': set()}
        module.add_dep('ctypes', False)
        module.add_dep('collections', 'OrderedDict')
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
        if len(dep_map['struct']) > 0:
            for dep_name in sorted(dep_map['struct']):
                module.add_dep('.._vulkan_type.%s' % dep_name, dep_name)
        if len(dep_map['callback']) > 0:
            for dep_name in sorted(dep_map['callback']):
                module.add_dep('.._vulkan_callback.%s' % dep_name, dep_name)
        if len(dep_map['enum']) > 0:
            for dep_name in sorted(dep_map['enum']):
                module.add_dep('.._vulkan_enum.%s' % dep_name, dep_name)
        module.append_lines('')
        return_status = info['return']['type'] == 'VkResult'
        if return_status:
            module.add_dep('.._vulkan_enum.VkResult', 'VkResult')
        return_arguments = [arg_name for arg_name in info['argument_list'] if info['argument_map'][arg_name]['output']]
        self._create_function_source(context, name, module)
        module.append_lines('')
        module.append_lines('%s._vulkan_ = {' % name)
        module.current_indent += 1
        module.append_lines('%r: {' % ('return'))
        module.current_indent += 1
        module.append_lines('%r: %r,' % ('type', info['return']['type']))
        module.append_lines('%r: %s,' % ('ctype', info['return']['ctype'].to_source()))
        module.append_lines('%r: %r,' % ('class', self._get_type_class(context, info['return']['type'])))
        module.append_lines('%r: %r,' % ('arguments', return_arguments))
        module.append_lines('%r: %r,' % ('status', return_status))
        if return_status:
            if 'success_code_list' in info:
                module.append_lines('%r: [%s],' % ('success', ', '.join(f'VkResult.{x}' for x in sorted(info['success_code_list']))))
            else:
                module.append_lines('%r: [],' % ('success'))
            if 'error_code_list' in info:
                module.append_lines('%r: [%s],' % ('error', ', '.join(f'VkResult.{x}' for x in sorted(info['error_code_list']))))
            else:
                module.append_lines('%r: [],' % ('error'))
        module.current_indent -= 1
        module.append_lines('},')
        module.append_lines('%r: OrderedDict([' % ('arguments'))
        module.current_indent += 1
        for arg_name in info['argument_list']:
            arg_info = info['argument_map'][arg_name]
            module.append_lines('(')
            module.current_indent += 1
            module.append_lines('%r,' % arg_name)
            module.append_lines('{')
            module.current_indent += 1
            module.append_lines('%r: %r,' % ('type', arg_info['type']))
            module.append_lines('%r: %s,' % ('ctype', arg_info['ctype'].to_source()))
            module.append_lines('%r: %r,' % ('class', self._get_type_class(context, arg_info['type'])))
            module.append_lines('%r: %r,' % ('output', arg_info['output'] if 'output' in arg_info else False))
            module.append_lines('%r: %r,' % ('is_string', arg_info['is_string'] if 'is_string' in arg_info else False))
            if 'cdecl' in arg_info:
                module.started_line = '%r: ' % ('cdecl')
                self._write_cdecl_source(context, module, arg_info['cdecl'])
            for attribute_name in arg_info['node'].attributes:
                module.append_lines('%r: %r,' % (f'@{attribute_name}', arg_info['node'].get_attribute(attribute_name)))
            module.append_lines('%r: %r,' % ('python_name', context.make_python_name(arg_name, skip_prefixes=('p', 'pp', 's'))))
            module.current_indent -= 1
            module.append_lines('},')
            module.current_indent -= 1
            module.append_lines('),')
        module.current_indent -= 1
        module.append_lines(']),')
        for attribute_name in info['node'].attributes:
            module.append_lines('%r: %r,' % (f'@{attribute_name}', info['node'].get_attribute(attribute_name)))
        module.current_indent -= 1
        module.append_lines('}')
        module.append_lines('')

        module.update_file(self.base_dir)

    def _write_vulkan_commands(self, context: Context):
        code = []
        for name in context.command_map:
            self._write_vulkan_command(context, name)
            code.append('from .%s import %s' % (name, name))
        alias_map = {k: v for k, v in context.alias_map.items() if v in context.command_map}
        for alias_name in sorted(alias_map.keys()):
            name = alias_map[alias_name]
            code.append('%s = %s' % (alias_name, name))
        code.append('')

        file = self.base_dir.joinpath('_vulkan_command/__init__.py')
        file.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_cdecl_source(self, context: Context, module: GeneratedModule, node: pycparser.c_ast.Node):
        module.add_dep('pycparser.c_ast', False, slot='import')
        module.append_lines('pycparser.c_ast.%s(' % node.__class__.__name__)
        module.current_indent += 1
        for attr in node.attr_names:
            value = getattr(node, attr)
            module.append_lines('%s=%r,' % (attr, value))
        for child_name, child in node.children():
            module.started_line = '%s=' % child_name
            self._write_cdecl_source(context, module, child)
        module.current_indent -= 1
        module.append_lines('),')

    def generate(self, context: Context):
        self.base_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
        self._write_vulkan_database(context)
        self._write_vulkan_enums(context)
        self._write_vulkan_value(context)
        self._write_vulkan_callbacks(context)
        self._write_vulkan_types(context)
        self._write_vulkan_handles(context)
        self._write_vulkan_commands(context)
