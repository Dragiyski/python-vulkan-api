import ctypes

class VkPhysicalDeviceGlobalPriorityQueryFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('globalPriorityQuery', ctypes.c_uint32),
    ]

VkPhysicalDeviceGlobalPriorityQueryFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'globalPriorityQuery': ctypes.c_uint32,
}
