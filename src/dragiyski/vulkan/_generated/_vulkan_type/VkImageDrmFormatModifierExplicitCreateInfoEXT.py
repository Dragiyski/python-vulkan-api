import ctypes, sys

class VkImageDrmFormatModifierExplicitCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageDrmFormatModifierExplicitCreateInfoEXT

from . import VkSubresourceLayout

VkImageDrmFormatModifierExplicitCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifier', ctypes.c_uint64),
    ('drmFormatModifierPlaneCount', ctypes.c_uint32),
    ('pPlaneLayouts', ctypes.POINTER(VkSubresourceLayout)),
]
