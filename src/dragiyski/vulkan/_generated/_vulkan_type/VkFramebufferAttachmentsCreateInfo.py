import ctypes

class VkFramebufferAttachmentsCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'attachmentImageInfoCount': ctypes.c_uint32,
            'pAttachmentImageInfos': ctypes.POINTER(VkFramebufferAttachmentImageInfo),
        }


from .VkFramebufferAttachmentImageInfo import VkFramebufferAttachmentImageInfo

VkFramebufferAttachmentsCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentImageInfoCount', ctypes.c_uint32),
    ('pAttachmentImageInfos', ctypes.POINTER(VkFramebufferAttachmentImageInfo)),
]
