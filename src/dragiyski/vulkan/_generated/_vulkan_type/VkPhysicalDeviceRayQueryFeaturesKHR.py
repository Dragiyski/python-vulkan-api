import ctypes

class VkPhysicalDeviceRayQueryFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayQuery', ctypes.c_uint32),
    ]

VkPhysicalDeviceRayQueryFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rayQuery': ctypes.c_uint32,
}
