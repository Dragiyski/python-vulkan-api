import ctypes, sys

class VkSparseImageMemoryRequirements2(ctypes.Structure):
    pass

sys.modules[__name__] = VkSparseImageMemoryRequirements2

from . import VkSparseImageMemoryRequirements

VkSparseImageMemoryRequirements2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryRequirements', VkSparseImageMemoryRequirements),
]
