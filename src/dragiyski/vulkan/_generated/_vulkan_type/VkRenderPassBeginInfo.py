import ctypes

class VkRenderPassBeginInfo(ctypes.Structure):
    pass

from .VkClearValue import VkClearValue
from .VkRect2D import VkRect2D

VkRenderPassBeginInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPass', ctypes.c_void_p),
    ('framebuffer', ctypes.c_void_p),
    ('renderArea', VkRect2D),
    ('clearValueCount', ctypes.c_uint32),
    ('pClearValues', ctypes.POINTER(VkClearValue)),
]

VkRenderPassBeginInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'renderPass': ctypes.c_void_p,
    'framebuffer': ctypes.c_void_p,
    'renderArea': VkRect2D,
    'clearValueCount': ctypes.c_uint32,
    'pClearValues': ctypes.POINTER(VkClearValue),
}
