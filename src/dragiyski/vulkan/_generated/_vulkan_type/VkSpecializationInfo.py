import ctypes

class CType(ctypes.Structure):
    pass

from .VkSpecializationMapEntry import CType as VkSpecializationMapEntry

CType._fields_ = [
    ('mapEntryCount', ctypes.c_uint32),
    ('pMapEntries', ctypes.POINTER(VkSpecializationMapEntry)),
    ('dataSize', ctypes.c_size_t),
    ('pData', ctypes.c_void_p),
]
