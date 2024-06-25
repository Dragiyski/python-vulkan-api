import ctypes

class VkSubresourceLayout2KHR(ctypes.Structure):
    pass

from .VkSubresourceLayout import VkSubresourceLayout

VkSubresourceLayout2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('subresourceLayout', VkSubresourceLayout),
]

VkSubresourceLayout2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'subresourceLayout': VkSubresourceLayout,
}
