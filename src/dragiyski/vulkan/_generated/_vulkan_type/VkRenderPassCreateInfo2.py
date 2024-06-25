import ctypes

class VkRenderPassCreateInfo2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'attachmentCount': ctypes.c_uint32,
            'pAttachments': ctypes.POINTER(VkAttachmentDescription2),
            'subpassCount': ctypes.c_uint32,
            'pSubpasses': ctypes.POINTER(VkSubpassDescription2),
            'dependencyCount': ctypes.c_uint32,
            'pDependencies': ctypes.POINTER(VkSubpassDependency2),
            'correlatedViewMaskCount': ctypes.c_uint32,
            'pCorrelatedViewMasks': ctypes.POINTER(ctypes.c_uint32),
        }


from .VkAttachmentDescription2 import VkAttachmentDescription2
from .VkSubpassDependency2 import VkSubpassDependency2
from .VkSubpassDescription2 import VkSubpassDescription2

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
