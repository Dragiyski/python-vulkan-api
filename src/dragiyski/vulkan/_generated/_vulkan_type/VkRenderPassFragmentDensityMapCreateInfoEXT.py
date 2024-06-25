import ctypes

class VkRenderPassFragmentDensityMapCreateInfoEXT(ctypes.Structure):
    pass

from .VkAttachmentReference import VkAttachmentReference

VkRenderPassFragmentDensityMapCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityMapAttachment', VkAttachmentReference),
]

VkRenderPassFragmentDensityMapCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentDensityMapAttachment': VkAttachmentReference,
}
