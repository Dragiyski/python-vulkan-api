import ctypes

class VkPhysicalDeviceCustomBorderColorFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('customBorderColors', ctypes.c_uint32),
        ('customBorderColorWithoutFormat', ctypes.c_uint32),
    ]

VkPhysicalDeviceCustomBorderColorFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'customBorderColors': ctypes.c_uint32,
    'customBorderColorWithoutFormat': ctypes.c_uint32,
}
