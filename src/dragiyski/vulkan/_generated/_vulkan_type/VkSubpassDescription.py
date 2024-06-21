import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentReference import CType as VkAttachmentReference

CType._fields_ = [
    ('flags', ctypes.c_uint32),
    ('pipelineBindPoint', ctypes.c_int),
    ('inputAttachmentCount', ctypes.c_uint32),
    ('pInputAttachments', ctypes.POINTER(VkAttachmentReference)),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkAttachmentReference)),
    ('pResolveAttachments', ctypes.POINTER(VkAttachmentReference)),
    ('pDepthStencilAttachment', ctypes.POINTER(VkAttachmentReference)),
    ('preserveAttachmentCount', ctypes.c_uint32),
    ('pPreserveAttachments', ctypes.POINTER(ctypes.c_uint32)),
]
