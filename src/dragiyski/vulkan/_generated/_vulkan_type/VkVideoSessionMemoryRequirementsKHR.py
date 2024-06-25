import ctypes

class VkVideoSessionMemoryRequirementsKHR(ctypes.Structure):
    pass

from .VkMemoryRequirements import VkMemoryRequirements

VkVideoSessionMemoryRequirementsKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryBindIndex', ctypes.c_uint32),
    ('memoryRequirements', VkMemoryRequirements),
]

VkVideoSessionMemoryRequirementsKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryBindIndex': ctypes.c_uint32,
    'memoryRequirements': VkMemoryRequirements,
}
