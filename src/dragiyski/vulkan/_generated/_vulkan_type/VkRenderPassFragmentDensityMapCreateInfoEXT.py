import ctypes, sys

class VkRenderPassFragmentDensityMapCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassFragmentDensityMapCreateInfoEXT

from . import VkAttachmentReference

VkRenderPassFragmentDensityMapCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityMapAttachment', VkAttachmentReference),
]
