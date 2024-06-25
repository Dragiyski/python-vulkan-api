import ctypes

class VkPhysicalDeviceVideoFormatInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageUsage', ctypes.c_uint32),
    ]

VkPhysicalDeviceVideoFormatInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageUsage': ctypes.c_uint32,
}
