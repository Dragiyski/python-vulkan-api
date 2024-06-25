import ctypes

class VkPhysicalDeviceDisplacementMicromapFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('displacementMicromap', ctypes.c_uint32),
    ]

VkPhysicalDeviceDisplacementMicromapFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'displacementMicromap': ctypes.c_uint32,
}
