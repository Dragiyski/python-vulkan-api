import ctypes

class VkRenderPassCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'attachmentCount': ctypes.c_uint32,
            'pAttachments': ctypes.POINTER(VkAttachmentDescription),
            'subpassCount': ctypes.c_uint32,
            'pSubpasses': ctypes.POINTER(VkSubpassDescription),
            'dependencyCount': ctypes.c_uint32,
            'pDependencies': ctypes.POINTER(VkSubpassDependency),
        }


from .VkAttachmentDescription import VkAttachmentDescription
from .VkSubpassDependency import VkSubpassDependency
from .VkSubpassDescription import VkSubpassDescription

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
