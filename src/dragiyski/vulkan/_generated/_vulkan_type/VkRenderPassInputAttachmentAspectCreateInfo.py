import ctypes

class VkRenderPassInputAttachmentAspectCreateInfo(ctypes.Structure):
    pass

from .VkInputAttachmentAspectReference import VkInputAttachmentAspectReference

VkRenderPassInputAttachmentAspectCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('aspectReferenceCount', ctypes.c_uint32),
    ('pAspectReferences', ctypes.POINTER(VkInputAttachmentAspectReference)),
]

VkRenderPassInputAttachmentAspectCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'aspectReferenceCount': ctypes.c_uint32,
    'pAspectReferences': ctypes.POINTER(VkInputAttachmentAspectReference),
}
