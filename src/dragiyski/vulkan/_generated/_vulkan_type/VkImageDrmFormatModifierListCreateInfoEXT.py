import ctypes

class VkImageDrmFormatModifierListCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('drmFormatModifierCount', ctypes.c_uint32),
        ('pDrmFormatModifiers', ctypes.POINTER(ctypes.c_uint64)),
    ]

VkImageDrmFormatModifierListCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'drmFormatModifierCount': ctypes.c_uint32,
    'pDrmFormatModifiers': ctypes.POINTER(ctypes.c_uint64),
}
