import ctypes

class VkPhysicalDeviceBorderColorSwizzleFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('borderColorSwizzle', ctypes.c_uint32),
        ('borderColorSwizzleFromImage', ctypes.c_uint32),
    ]

VkPhysicalDeviceBorderColorSwizzleFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'borderColorSwizzle': ctypes.c_uint32,
    'borderColorSwizzleFromImage': ctypes.c_uint32,
}
