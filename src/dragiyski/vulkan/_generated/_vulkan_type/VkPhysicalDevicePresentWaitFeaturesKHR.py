import ctypes

class VkPhysicalDevicePresentWaitFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentWait', ctypes.c_uint32),
    ]

VkPhysicalDevicePresentWaitFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentWait': ctypes.c_uint32,
}
