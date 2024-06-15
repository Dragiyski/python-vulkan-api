import ctypes, sys

class VkCommandBufferInheritanceViewportScissorInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkCommandBufferInheritanceViewportScissorInfoNV

from . import VkViewport

VkCommandBufferInheritanceViewportScissorInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportScissor2D', ctypes.c_uint32),
    ('viewportDepthCount', ctypes.c_uint32),
    ('pViewportDepths', ctypes.POINTER(VkViewport)),
]
