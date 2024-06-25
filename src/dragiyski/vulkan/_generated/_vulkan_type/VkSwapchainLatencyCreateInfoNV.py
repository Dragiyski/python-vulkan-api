import ctypes

class VkSwapchainLatencyCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('latencyModeEnable', ctypes.c_uint32),
    ]

VkSwapchainLatencyCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'latencyModeEnable': ctypes.c_uint32,
}
