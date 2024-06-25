import ctypes

class VkPhysicalDevicePresentIdFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentId', ctypes.c_uint32),
    ]

VkPhysicalDevicePresentIdFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentId': ctypes.c_uint32,
}
