import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseImageMemoryRequirements import CType as VkSparseImageMemoryRequirements

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryRequirements', VkSparseImageMemoryRequirements),
]
