import ctypes, sys

class VkRenderPassInputAttachmentAspectCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassInputAttachmentAspectCreateInfo

from . import VkInputAttachmentAspectReference

VkRenderPassInputAttachmentAspectCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('aspectReferenceCount', ctypes.c_uint32),
    ('pAspectReferences', ctypes.POINTER(VkInputAttachmentAspectReference)),
]
