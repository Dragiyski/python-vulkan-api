import ctypes

class VkSwapchainPresentBarrierCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentBarrierEnable', ctypes.c_uint32),
    ]

VkSwapchainPresentBarrierCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentBarrierEnable': ctypes.c_uint32,
}
