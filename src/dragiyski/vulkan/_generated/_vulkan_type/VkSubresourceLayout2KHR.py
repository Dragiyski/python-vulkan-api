import ctypes, sys

class VkSubresourceLayout2KHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkSubresourceLayout2KHR

from . import VkSubresourceLayout

VkSubresourceLayout2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('subresourceLayout', VkSubresourceLayout),
]
