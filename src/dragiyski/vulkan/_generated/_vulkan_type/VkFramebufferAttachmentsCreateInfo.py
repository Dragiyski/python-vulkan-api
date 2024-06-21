import ctypes

class CType(ctypes.Structure):
    pass

from .VkFramebufferAttachmentImageInfo import CType as VkFramebufferAttachmentImageInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentImageInfoCount', ctypes.c_uint32),
    ('pAttachmentImageInfos', ctypes.POINTER(VkFramebufferAttachmentImageInfo)),
]
