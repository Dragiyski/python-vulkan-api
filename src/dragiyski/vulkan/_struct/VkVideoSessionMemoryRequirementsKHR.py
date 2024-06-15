import ctypes, sys

class VkVideoSessionMemoryRequirementsKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoSessionMemoryRequirementsKHR

from . import VkMemoryRequirements

VkVideoSessionMemoryRequirementsKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryBindIndex', ctypes.c_uint32),
    ('memoryRequirements', VkMemoryRequirements),
]
