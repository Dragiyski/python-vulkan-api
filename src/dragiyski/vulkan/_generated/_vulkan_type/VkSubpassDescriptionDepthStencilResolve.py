import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentReference2 import CType as VkAttachmentReference2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('depthResolveMode', ctypes.c_uint32),
    ('stencilResolveMode', ctypes.c_uint32),
    ('pDepthStencilResolveAttachment', ctypes.POINTER(VkAttachmentReference2)),
]
