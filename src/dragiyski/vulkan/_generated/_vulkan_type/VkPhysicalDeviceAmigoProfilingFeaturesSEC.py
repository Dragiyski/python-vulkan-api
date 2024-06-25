import ctypes

class VkPhysicalDeviceAmigoProfilingFeaturesSEC(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('amigoProfiling', ctypes.c_uint32),
    ]

VkPhysicalDeviceAmigoProfilingFeaturesSEC._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'amigoProfiling': ctypes.c_uint32,
}
