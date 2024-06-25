import ctypes

class VkPhysicalDeviceFragmentShaderBarycentricFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentShaderBarycentric', ctypes.c_uint32),
    ]

VkPhysicalDeviceFragmentShaderBarycentricFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentShaderBarycentric': ctypes.c_uint32,
}
