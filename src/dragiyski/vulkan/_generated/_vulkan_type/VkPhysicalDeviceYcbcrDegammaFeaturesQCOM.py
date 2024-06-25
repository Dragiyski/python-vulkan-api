import ctypes

class VkPhysicalDeviceYcbcrDegammaFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('ycbcrDegamma', ctypes.c_uint32),
    ]

VkPhysicalDeviceYcbcrDegammaFeaturesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'ycbcrDegamma': ctypes.c_uint32,
}
