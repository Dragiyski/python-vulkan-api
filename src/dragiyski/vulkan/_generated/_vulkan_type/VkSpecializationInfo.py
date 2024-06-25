import ctypes

class VkSpecializationInfo(ctypes.Structure):
    pass

from .VkSpecializationMapEntry import VkSpecializationMapEntry

VkSpecializationInfo._fields_ = [
    ('mapEntryCount', ctypes.c_uint32),
    ('pMapEntries', ctypes.POINTER(VkSpecializationMapEntry)),
    ('dataSize', ctypes.c_size_t),
    ('pData', ctypes.c_void_p),
]

VkSpecializationInfo._type_ = {
    'mapEntryCount': ctypes.c_uint32,
    'pMapEntries': ctypes.POINTER(VkSpecializationMapEntry),
    'dataSize': ctypes.c_size_t,
    'pData': ctypes.c_void_p,
}
