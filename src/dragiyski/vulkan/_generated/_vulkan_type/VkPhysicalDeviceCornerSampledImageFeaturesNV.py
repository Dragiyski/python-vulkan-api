import ctypes

class VkPhysicalDeviceCornerSampledImageFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cornerSampledImage', ctypes.c_uint32),
    ]

VkPhysicalDeviceCornerSampledImageFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'cornerSampledImage': ctypes.c_uint32,
}
