import ctypes, sys

class VkDeviceImageMemoryRequirements(ctypes.Structure):
    pass

sys.modules[__name__] = VkDeviceImageMemoryRequirements

from . import VkImageCreateInfo

VkDeviceImageMemoryRequirements._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('planeAspect', ctypes.c_uint32),
]