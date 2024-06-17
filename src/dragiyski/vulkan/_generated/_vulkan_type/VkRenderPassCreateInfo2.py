import ctypes, sys

class VkRenderPassCreateInfo2(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassCreateInfo2

from . import VkAttachmentDescription2
from . import VkSubpassDependency2
from . import VkSubpassDescription2

VkRenderPassCreateInfo2._fields_ = [
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
