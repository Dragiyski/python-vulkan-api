import ctypes

class CType(ctypes.Structure):
    pass

from .VkMemoryRequirements import CType as VkMemoryRequirements

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryBindIndex', ctypes.c_uint32),
    ('memoryRequirements', VkMemoryRequirements),
]
