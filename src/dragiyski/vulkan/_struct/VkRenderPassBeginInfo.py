import ctypes, sys

class VkRenderPassBeginInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassBeginInfo

from . import VkRect2D
from . import VkClearValue

VkRenderPassBeginInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPass', ctypes.c_void_p),
    ('framebuffer', ctypes.c_void_p),
    ('renderArea', VkRect2D),
    ('clearValueCount', ctypes.c_uint32),
    ('pClearValues', ctypes.POINTER(VkClearValue)),
]
