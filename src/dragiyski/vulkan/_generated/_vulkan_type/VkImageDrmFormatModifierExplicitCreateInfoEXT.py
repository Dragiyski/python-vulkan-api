import ctypes

class VkImageDrmFormatModifierExplicitCreateInfoEXT(ctypes.Structure):
    pass

from .VkSubresourceLayout import VkSubresourceLayout

VkImageDrmFormatModifierExplicitCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifier', ctypes.c_uint64),
    ('drmFormatModifierPlaneCount', ctypes.c_uint32),
    ('pPlaneLayouts', ctypes.POINTER(VkSubresourceLayout)),
]

VkImageDrmFormatModifierExplicitCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'drmFormatModifier': ctypes.c_uint64,
    'drmFormatModifierPlaneCount': ctypes.c_uint32,
    'pPlaneLayouts': ctypes.POINTER(VkSubresourceLayout),
}
