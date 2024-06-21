import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentReference2 import CType as VkAttachmentReference2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pipelineBindPoint', ctypes.c_int),
    ('viewMask', ctypes.c_uint32),
    ('inputAttachmentCount', ctypes.c_uint32),
    ('pInputAttachments', ctypes.POINTER(VkAttachmentReference2)),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkAttachmentReference2)),
    ('pResolveAttachments', ctypes.POINTER(VkAttachmentReference2)),
    ('pDepthStencilAttachment', ctypes.POINTER(VkAttachmentReference2)),
    ('preserveAttachmentCount', ctypes.c_uint32),
    ('pPreserveAttachments', ctypes.POINTER(ctypes.c_uint32)),
]
