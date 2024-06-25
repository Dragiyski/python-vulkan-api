import ctypes

class VkPhysicalDeviceIndexTypeUint8FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('indexTypeUint8', ctypes.c_uint32),
    ]

VkPhysicalDeviceIndexTypeUint8FeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'indexTypeUint8': ctypes.c_uint32,
}
