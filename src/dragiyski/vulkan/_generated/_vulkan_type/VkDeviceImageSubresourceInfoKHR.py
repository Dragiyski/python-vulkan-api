import ctypes

class VkDeviceImageSubresourceInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pCreateInfo': ctypes.POINTER(VkImageCreateInfo),
            'pSubresource': ctypes.POINTER(VkImageSubresource2KHR),
        }


from .VkImageCreateInfo import VkImageCreateInfo
from .VkImageSubresource2KHR import VkImageSubresource2KHR

VkDeviceImageSubresourceInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('pSubresource', ctypes.POINTER(VkImageSubresource2KHR)),
]
