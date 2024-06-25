import ctypes

class VkSparseImageMemoryRequirements2(ctypes.Structure):
    pass

from .VkSparseImageMemoryRequirements import VkSparseImageMemoryRequirements

VkSparseImageMemoryRequirements2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryRequirements', VkSparseImageMemoryRequirements),
]

VkSparseImageMemoryRequirements2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryRequirements': VkSparseImageMemoryRequirements,
}
