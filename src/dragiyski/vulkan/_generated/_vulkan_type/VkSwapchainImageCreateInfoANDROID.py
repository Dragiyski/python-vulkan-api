import ctypes, sys

class VkSwapchainImageCreateInfoANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('usage', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSwapchainImageCreateInfoANDROID
