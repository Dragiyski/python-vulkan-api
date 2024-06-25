import ctypes

class VkFramebufferAttachmentsCreateInfo(ctypes.Structure):
    pass

from .VkFramebufferAttachmentImageInfo import VkFramebufferAttachmentImageInfo

VkFramebufferAttachmentsCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentImageInfoCount', ctypes.c_uint32),
    ('pAttachmentImageInfos', ctypes.POINTER(VkFramebufferAttachmentImageInfo)),
]

VkFramebufferAttachmentsCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'attachmentImageInfoCount': ctypes.c_uint32,
    'pAttachmentImageInfos': ctypes.POINTER(VkFramebufferAttachmentImageInfo),
}
