import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentDescription2 import CType as VkAttachmentDescription2
from .VkSubpassDependency2 import CType as VkSubpassDependency2
from .VkSubpassDescription2 import CType as VkSubpassDescription2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('attachmentCount', ctypes.c_uint32),
    ('pAttachments', ctypes.POINTER(VkAttachmentDescription2)),
    ('subpassCount', ctypes.c_uint32),
    ('pSubpasses', ctypes.POINTER(VkSubpassDescription2)),
    ('dependencyCount', ctypes.c_uint32),
    ('pDependencies', ctypes.POINTER(VkSubpassDependency2)),
    ('correlatedViewMaskCount', ctypes.c_uint32),
    ('pCorrelatedViewMasks', ctypes.POINTER(ctypes.c_uint32)),
]