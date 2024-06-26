import ctypes
from collections import namedtuple

from .._pointer import finalize, PointerStorageType
from .. import binding
from ..version import *

_structure_unchain = {
    'VkPhysicalDeviceProperties2': {}
}

for base_name in _structure_unchain:
    base_target = _structure_unchain[base_name]
    for name in getattr(binding.VkPhysicalDeviceProperties2, '_extended_by_', ()):
        struct = getattr(binding, name, None)
        if struct is not None:
            struct_type = getattr(struct, '_vk_structure_type_', None)
            if isinstance(struct_type, str) and struct_type.startswith('VK_STRUCTURE_TYPE_') and hasattr(binding.VkStructureType, struct_type):
                base_target[getattr(binding.VkStructureType, struct_type)] = struct
            del struct_type
        del struct, name
    del base_target, base_name


def _process_structure(structure, *, _unchain = True):
    fields = [x[0] for x in structure._fields_]
    kv = dict()
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
            value = _process_structure(value)
        elif isinstance(value, ctypes.Array):
            value = list(value)
        elif (ctype is ctypes.c_char_p or issubclass(ctype, ctypes.Array) and ctype._type_ is ctypes.c_char) and isinstance(value, bytes):
            value = value.decode()
        if structure.__class__.__name__ in _special_structure_value:
            if field in _special_structure_value[structure.__class__.__name__]:
                value = _special_structure_value[structure.__class__.__name__][field](value)
        kv[name] = value
    if structure.__class__.__name__ in _structure_unchain:
        last_structure = structure
        while last_structure.pNext is not None:
            struct_type = ctypes.cast(last_structure.pNext, ctypes.POINTER(binding.VkBaseOutStructure)).contents.sType
            if struct_type not in _structure_unchain[structure.__class__.__name__]:
                raise ReferenceError('Structure %s refers to address 0x%016x containing unknown/unexpected structure type: %d' % (
                    last_structure.__class__.__name__,
                    last_structure.pNext,
                    struct_type
                ))
            struct_class = _structure_unchain[structure.__class__.__name__][struct_type]
            this_struct = ctypes.cast(ctypes.c_void_p(last_structure.pNext), ctypes.POINTER(struct_class)).contents
            kv[struct_class.__name__] = _process_structure(this_struct, _unchain = False)
            last_structure = this_struct
    
    postprocess = _struct_postprocess_dictionary.get(structure.__class__.__name__, None)
    if callable(postprocess):
        kv = postprocess(kv)
    kv['__name__'] = structure.__class__.__name__
    return kv

def _process_VkPhysicalDeviceProperties2(kv):
    properties = kv['properties']
    del kv['properties']
    kv.update(properties)
    return kv

_special_structure_value = {
    'VkPhysicalDeviceProperties': {
        'apiVersion': lambda value: VkApiVersion(value)
    }
}

_struct_postprocess_dictionary = {
    'VkPhysicalDeviceProperties2': _process_VkPhysicalDeviceProperties2
}

def _postprocess_dictionary(kv):
    for k, v in kv.items():
        if isinstance(v, dict) and '__name__' in v:
            kv[k] = _postprocess_dictionary(v)
    name = kv['__name__']
    del kv['__name__']
    return namedtuple(name, kv.keys())(*kv.values())

class VkPhysicalDevice(metaclass = PointerStorageType):
    def _get_properties(self):
        vkGetPhysicalDeviceProperties = self._loader_.vkGetPhysicalDeviceProperties
        properties = binding.VkPhysicalDeviceProperties()
        vkGetPhysicalDeviceProperties(self, ctypes.byref(properties))
        return _postprocess_dictionary(_process_structure(properties))
    
    def _get_properties_2(self):
        try:
            vkGetPhysicalDeviceProperties2 = self._loader_.vkGetPhysicalDeviceProperties2
        except AttributeError:
            raise NotImplementedError('vkGetPhysicalDeviceProperties2') from None

        vk_version = self._loader_.instance.application.enumerate_instance_version()
        properties = binding.VkPhysicalDeviceProperties2()
        last_struct = properties
        for struct_name in getattr(properties, '_extended_by_', ()):
            extend_struct_class = getattr(binding, struct_name, None)
            if issubclass(extend_struct_class, ctypes.Structure):
                fields = [s[0] for s in extend_struct_class._fields_]
                has_version = False
                version_test = True
                has_extension = False
                extension_test = True
                if 'sType' in fields and 'pNext' in fields:
                    if hasattr(extend_struct_class, '_vk_versions_') and len(extend_struct_class._vk_versions_) > 0:
                        has_version = True
                        min_version = [0, 0, 0]
                        for feature_version in extend_struct_class._vk_versions_:
                            for i, v in enumerate(feature_version[:3]):
                                min_version[i] = max(min_version[i], v)
                        for i, n in enumerate(['major', 'minor', 'patch']):
                            if min_version[i] > getattr(vk_version, n):
                                version_test = False
                    if hasattr(extend_struct_class, '_vk_extensions_') and len(extend_struct_class._vk_extensions_) > 0:
                        has_extension = True
                        if not set(self._loader_.instance.extensions).intersection(extend_struct_class._vk_extensions_):
                            extension_test = False
                    if has_version and not version_test or has_extension and not extension_test:
                        continue
                    struct = extend_struct_class()
                    last_struct.pNext = ctypes.cast(ctypes.pointer(struct), ctypes.c_void_p)
                    last_struct = struct
        vkGetPhysicalDeviceProperties2(self, ctypes.byref(properties))
        return _postprocess_dictionary(_process_structure(properties))

    def get_properties(self):
        for fn in (self._get_properties_2, self._get_properties):
            try:
                return fn()
            except NotImplementedError as error:
                continue
        raise error
