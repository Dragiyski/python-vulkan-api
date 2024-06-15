import ctypes, sys

class VkRenderPassCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassCreateInfo

from . import VkAttachmentDescription
from . import VkSubpassDependency
from . import VkSubpassDescription

VkRenderPassCreateInfo._fields_ = [
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
