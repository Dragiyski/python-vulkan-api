import ctypes, sys

class VkFramebufferAttachmentsCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkFramebufferAttachmentsCreateInfo

from . import VkFramebufferAttachmentImageInfo

VkFramebufferAttachmentsCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentImageInfoCount', ctypes.c_uint32),
    ('pAttachmentImageInfos', ctypes.POINTER(VkFramebufferAttachmentImageInfo)),
]
