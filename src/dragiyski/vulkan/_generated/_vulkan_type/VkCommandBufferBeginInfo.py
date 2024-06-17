import ctypes, sys

class VkCommandBufferBeginInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkCommandBufferBeginInfo

from . import VkCommandBufferInheritanceInfo

VkCommandBufferBeginInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pInheritanceInfo', ctypes.POINTER(VkCommandBufferInheritanceInfo)),
]
