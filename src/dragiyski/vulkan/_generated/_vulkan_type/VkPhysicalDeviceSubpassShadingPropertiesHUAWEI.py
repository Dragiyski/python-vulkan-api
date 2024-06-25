import ctypes

class VkPhysicalDeviceSubpassShadingPropertiesHUAWEI(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxSubpassShadingWorkgroupSizeAspectRatio', ctypes.c_uint32),
    ]

VkPhysicalDeviceSubpassShadingPropertiesHUAWEI._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxSubpassShadingWorkgroupSizeAspectRatio': ctypes.c_uint32,
}
