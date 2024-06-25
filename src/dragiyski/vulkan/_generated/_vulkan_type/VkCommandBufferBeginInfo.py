import ctypes

class VkCommandBufferBeginInfo(ctypes.Structure):
    pass

from .VkCommandBufferInheritanceInfo import VkCommandBufferInheritanceInfo

VkCommandBufferBeginInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pInheritanceInfo', ctypes.POINTER(VkCommandBufferInheritanceInfo)),
]

VkCommandBufferBeginInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pInheritanceInfo': ctypes.POINTER(VkCommandBufferInheritanceInfo),
}
