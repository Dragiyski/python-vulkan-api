import ctypes

class VkPhysicalDeviceSubpassShadingFeaturesHUAWEI(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subpassShading', ctypes.c_uint32),
    ]

VkPhysicalDeviceSubpassShadingFeaturesHUAWEI._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'subpassShading': ctypes.c_uint32,
}
