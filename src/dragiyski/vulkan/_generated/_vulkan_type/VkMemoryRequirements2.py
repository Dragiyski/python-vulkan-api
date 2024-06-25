import ctypes

class VkMemoryRequirements2(ctypes.Structure):
    pass

from .VkMemoryRequirements import VkMemoryRequirements

VkMemoryRequirements2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryRequirements', VkMemoryRequirements),
]

VkMemoryRequirements2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryRequirements': VkMemoryRequirements,
}
