import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D
from .VkRenderingAttachmentInfo import CType as VkRenderingAttachmentInfo

CType._fields_ = [
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
