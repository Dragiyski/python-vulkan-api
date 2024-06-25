import ctypes

class VkPhysicalDeviceCustomBorderColorPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxCustomBorderColorSamplers', ctypes.c_uint32),
    ]

VkPhysicalDeviceCustomBorderColorPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxCustomBorderColorSamplers': ctypes.c_uint32,
}
