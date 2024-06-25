import ctypes

class VkPhysicalDeviceShaderImageFootprintFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageFootprint', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderImageFootprintFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageFootprint': ctypes.c_uint32,
}
