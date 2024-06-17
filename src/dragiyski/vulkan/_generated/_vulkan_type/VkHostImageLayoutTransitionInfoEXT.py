import ctypes, sys

class VkHostImageLayoutTransitionInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkHostImageLayoutTransitionInfoEXT

from . import VkImageSubresourceRange

VkHostImageLayoutTransitionInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('image', ctypes.c_void_p),
    ('oldLayout', ctypes.c_int),
    ('newLayout', ctypes.c_int),
    ('subresourceRange', VkImageSubresourceRange),
]
