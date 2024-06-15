import ctypes, sys

class VkDeviceImageSubresourceInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkDeviceImageSubresourceInfoKHR

from . import VkImageSubresource2KHR
from . import VkImageCreateInfo

VkDeviceImageSubresourceInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('pSubresource', ctypes.POINTER(VkImageSubresource2KHR)),
]
