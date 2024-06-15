import ctypes, sys

class VkRenderingInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderingInfo

from . import VkRect2D
from . import VkRenderingAttachmentInfo

VkRenderingInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('renderArea', VkRect2D),
    ('layerCount', ctypes.c_uint32),
    ('viewMask', ctypes.c_uint32),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkRenderingAttachmentInfo)),
    ('pDepthAttachment', ctypes.POINTER(VkRenderingAttachmentInfo)),
    ('pStencilAttachment', ctypes.POINTER(VkRenderingAttachmentInfo)),
]
