import sys, pathlib, ctypes
from os import linesep
src_path = pathlib.Path(__file__).resolve().parent.parent.joinpath('src')
sys.path.append(str(src_path))
from dragiyski.vulkan.binding import type as vulkan_type, enum as vulkan_enum
from dragiyski.vulkan import _ctypes

def get_pointer_length_source(ptr_type: _ctypes.CPointerType, length_info: list[str]):
    if not isinstance(ptr_type, _ctypes.CPointerType):
        return ptr_type.get_hint_source()
    if len(length_info) <= 0:
        return ptr_type.get_hint_source()
    length_desc = length_info[0]
    if length_desc == 'null-terminated':
        return ptr_type.get_hint_source()
    try:
        length_value = int(length_desc, 10)
        return ptr_type.get_hint_source()
    except ValueError:
        pass
    # The length is not a number or "null-terminated", then it must be field reference.
    # Then we expect this to be an array.
    sub_hint = get_pointer_length_source(ptr_type.type, length_info[1:])
    return 'ctypes.Array[%s] | Collection[%s]' % (sub_hint, sub_hint)

def generate_vulkan_type_hints():
    deps = {
        'ctypes': {False}
    }
    hint = {}
    for name in dir(vulkan_type):
        if name.startswith('_'):
            continue
        type_class = getattr(vulkan_type, name)
        lines = ['class %s(ctypes.%s):' % (name, type_class.__base__.__name__)]
        for member_name, member_type in type_class._vulkan_ctype_.fields.items():
            member_type: _ctypes.CType
            member_info = type_class._vulkan_fields_[member_name]
            if member_info['type']['class'] == 'enum':
                member_type.append_hint_deps(deps)
                if '.enum' not in deps:
                    deps['.enum'] = set()
                deps['.enum'].add(member_info['type']['name'])
                lines.append('    %s: %s | %s' % (member_name, member_info['type']['name'], member_type.get_hint_source()))
            elif 'length' in member_info and len([x for x in member_info['length'] if x != 'null-terminated']) > 0:
                member_type.append_hint_deps(deps)
                if 'collections.abc' not in deps:
                    deps['collections.abc'] = set()
                deps['collections.abc'].add('Collection')
                lines.append('    %s: %s' % (member_name, get_pointer_length_source(member_type, member_info['length'])))
            elif member_info['type']['class'] == 'callback' and isinstance(member_type, _ctypes.CFunctionType):
                if '.callback' not in deps:
                    deps['.callback'] = set()
                deps['.callback'].add(member_type.name)
                lines.append('    %s: %s' % (member_name, member_type.get_hint_source()))
            elif member_info['type']['class'] == 'command' and isinstance(member_type, _ctypes.CFunctionType):
                if '.command' not in deps:
                    deps['.command'] = set()
                deps['.command'].add(member_type.name)
                lines.append('    %s: %s' % (member_name, member_type.get_hint_source()))
            else:
                member_type.append_hint_deps(deps)
                lines.append('    %s: %s' % (member_name, member_type.get_hint_source()))
        lines.append('')
        hint[name] = lines
    pdeps = {}
    for mod, ns in deps.items():
        if mod.startswith('dragiyski.vulkan._generated._vulkan_type.') and len(ns) == 1 and all(isinstance(x, str) for x in ns):
            continue # All hints for vulkan types will be in this file
        else:
            pdeps[mod] = ns
    code = []
    for mod, ns in pdeps.items():
        if False in ns:
            code.append('import %s' % mod)
        if True in ns:
            code.append('from %s import *' % mod)
        names = {x for x in ns if isinstance(x, str)}
        if len(names) > 1:
            code.append('from %s import (' % mod)
            for name in sorted(names):
                code.append('    %s,' % name)
            code.append(')')
        elif len(names) > 0:
            code.append('from %s import %s' % (mod, ', '.join(names)))
    code.append('')
    for hint_name in sorted(hint.keys()):
        hint_lines = hint[hint_name]
        code.extend(hint_lines)
    
    file = src_path.joinpath('dragiyski/vulkan/binding/type.pyi')
    with open(file, 'w') as stream:
        stream.write(linesep.join(code))

def main():
    generate_vulkan_type_hints()
    return 0

if __name__ == '__main__':
    sys.exit(main())