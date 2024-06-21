import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentDescription import CType as VkAttachmentDescription
from .VkSubpassDependency import CType as VkSubpassDependency
from .VkSubpassDescription import CType as VkSubpassDescription

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('attachmentCount', ctypes.c_uint32),
    ('pAttachments', ctypes.POINTER(VkAttachmentDescription)),
    ('subpassCount', ctypes.c_uint32),
    ('pSubpasses', ctypes.POINTER(VkSubpassDescription)),
    ('dependencyCount', ctypes.c_uint32),
    ('pDependencies', ctypes.POINTER(VkSubpassDependency)),
]
