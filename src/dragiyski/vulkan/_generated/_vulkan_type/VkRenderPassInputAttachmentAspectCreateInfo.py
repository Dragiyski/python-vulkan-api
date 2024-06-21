import ctypes

class CType(ctypes.Structure):
    pass

from .VkInputAttachmentAspectReference import CType as VkInputAttachmentAspectReference

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('aspectReferenceCount', ctypes.c_uint32),
    ('pAspectReferences', ctypes.POINTER(VkInputAttachmentAspectReference)),
]
