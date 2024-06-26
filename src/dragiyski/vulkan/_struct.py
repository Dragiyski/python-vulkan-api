import ctypes
from collections.abc import Iterable, Mapping, Callable
from . import binding
from .version import *

def _enumerate_struct_stype_map():
    from ._generated import vulkan_type
    type_map = { n: getattr(vulkan_type, n) for n in dir(vulkan_type) if not n.startswith('_') }
    type_map = { k: v for k, v in type_map.items() if issubclass(v, ctypes.Structure) and isinstance(getattr(v, '_type_', None), dict) and 'sType' in v._type_ and isinstance(getattr(v, '_vk_structure_type_', None), str) }
    stype_map = { getattr(binding.VkStructureType, v._vk_structure_type_): v for v in type_map.values() }
    binding.VkPhysicalDeviceFeatures2
    return stype_map

_stype_map = _enumerate_struct_stype_map()
del _enumerate_struct_stype_map

def build_out_struct_chain(structure: ctypes.Structure, version: VkApiVersion, extensions: Iterable[str]) -> ctypes.Structure:
    extensions = set(extensions)
    last_structure = structure
    for struct_name in getattr(structure, '_extended_by_', ()):
        NextStructure = getattr(binding, struct_name, None)
        if issubclass(NextStructure, ctypes.Structure):
            fields = [s[0] for s in NextStructure._fields_]
            if 'sType' in fields and 'pNext' in fields:
                has_version = False
                version_test = True
                has_extension = False
                extension_test = True
                if hasattr(NextStructure, '_vk_versions_') and len(NextStructure._vk_versions_) > 0:
                    has_version = True
                    ns_version = min(VkApiVersion.create(0, *v) for v in NextStructure._vk_versions_)
                    if ns_version > version:
                        version_test = False
                if hasattr(NextStructure, '_vk_extensions_') and len(NextStructure._vk_extensions_) > 0:
                    has_extension = True
                    if not extensions.intersection(NextStructure._vk_extensions_):
                        extension_test = False
                if has_version and not version_test or has_extension and not extension_test:
                    continue
                next_structure = NextStructure()
                last_structure.pNext = ctypes.cast(ctypes.pointer(next_structure), ctypes.c_void_p)
                last_structure = next_structure

class StructureChainDuplicateConflictError(RuntimeError):
    pass

def dictify_unchain_strcuture(structure, unchain, /, dict_processor: Mapping[str, Callable] = {}, value_processor: Mapping[str, Mapping[str, Callable]] = {}) -> dict:
    fields = [x[0] for x in structure._fields_]
    mapping = dict()

    for field in fields:
        if field in ['sType', 'pNext']:
            continue
        value = getattr(structure, field)
        if field in getattr(structure, '_vk_enum_', {}):
            enum = getattr(binding, structure._vk_enum_[field], None)
            if enum is not None:
                try:
                    value = enum(value)
                except ValueError:
                    pass
        name = field
        if name in getattr(structure, '_python_name_', {}):
            name = structure._python_name_[name]
        ctype = getattr(structure, '_type_', {}).get(field, None)
        if isinstance(value, ctypes.Structure) or isinstance(value, ctypes.Union):
            value = dictify_unchain_strcuture(value, False, dict_processor = dict_processor, value_processor = value_processor)
        elif isinstance(value, ctypes.Array):
            value = list(value)
        elif (ctype is ctypes.c_char_p or issubclass(ctype, ctypes.Array) and ctype._type_ is ctypes.c_char) and isinstance(value, bytes):
            value = value.decode()
        strcuture_value_processor = value_processor.get(type(structure).__name__, None)
        if isinstance(strcuture_value_processor, Mapping):
            this_value_processor = strcuture_value_processor.get(field, None)
            if callable(this_value_processor):
                value = this_value_processor(value)
        mapping[name] = value
    if unchain and 'sType' in fields and 'pNext' in fields:
        last_structure = structure
        while last_structure.pNext is not None:
            this_structure_type = ctypes.cast(last_structure.pNext, ctypes.POINTER(binding.VkBaseOutStructure)).contents.sType
            if this_structure_type in _stype_map:
                this_structure_class = _stype_map[this_structure_type]
                this_structure_name = this_structure_class.__name__
                if this_structure_name in mapping:
                    # TODO: This might be supported behavior. Maybe replace the element with a list?
                    raise StructureChainDuplicateConflictError('More than one structure "%s" found in the structure chain.' % this_structure_name)
                this_structure = ctypes.cast(ctypes.c_void_p(last_structure.pNext), ctypes.POINTER(this_structure_class)).contents
                mapping[this_structure_name] = dictify_unchain_strcuture(this_structure, False, dict_processor = dict_processor, value_processor = value_processor)
                last_structure = this_structure
    
    structure_name = type(structure).__name__
    mapping['__name__'] = structure_name
    mapping['_as_parameter_'] = structure
    structure_dict_processor = dict_processor.get(structure_name, None)
    if callable(structure_dict_processor):
        return structure_dict_processor(mapping)
    return mapping

_data_type = {}

def pythonify_dict(kv: Mapping):
    for k, v in kv.items():
        if isinstance(v, dict) and '__name__' in v:
            kv[k] = pythonify_dict(v)
    name = kv['__name__']
    del kv['__name__']
    if name not in _data_type:
        Structure = getattr(binding, name)
        _data_type[name] = type(name, (), {
            '__module__': Structure.__module__
        })
    self = _data_type[name]()
    self.__dict__.update(kv)
    return self

def pythonify_unchain_structure(structure, /, *args, **kwargs):
    return pythonify_dict(dictify_unchain_strcuture(structure, True, *args, **kwargs))

def get_chain_map(name: str):
    if name not in _chain_map_cache:
        chain_map = {}
        base_struct = getattr(binding, name, None)
        # Only structures can be chained, unions cannot be chained.
        # TODO: Check if we there are Union of Structure(s), which can be chained on any of its structures, when the structures are represented by VkBase(In|Out)Structure.
        if not isinstance(base_struct, ctypes.Structure):
            raise TypeError('Invalid structure name "%s": not a ctypes.Structure instance.')
        for name in getattr(base_struct, '_extended_by_', ()):
            struct = getattr(binding, name, None)
            if struct is not None:
                struct_type = getattr(struct, '_vk_structure_type_', None)
                if isinstance(struct_type, str) and struct_type.startswith('VK_STRUCTURE_TYPE_') and hasattr(binding.VkStructureType, struct_type):
                    base_target[getattr(binding.VkStructureType, struct_type)] = struct
