import ctypes, sys

class VkSwapchainPresentBarrierCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentBarrierEnable', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSwapchainPresentBarrierCreateInfoNV
