import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentReference import CType as VkAttachmentReference

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityMapAttachment', VkAttachmentReference),
]
