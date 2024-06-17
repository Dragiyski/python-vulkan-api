import ctypes, sys

class VkMemoryRequirements2(ctypes.Structure):
    pass

sys.modules[__name__] = VkMemoryRequirements2

from . import VkMemoryRequirements

VkMemoryRequirements2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryRequirements', VkMemoryRequirements),
]
