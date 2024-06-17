import ctypes, sys

class VkSpecializationInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkSpecializationInfo

from . import VkSpecializationMapEntry

VkSpecializationInfo._fields_ = [
    ('mapEntryCount', ctypes.c_uint32),
    ('pMapEntries', ctypes.POINTER(VkSpecializationMapEntry)),
    ('dataSize', ctypes.c_size_t),
    ('pData', ctypes.c_void_p),
]
