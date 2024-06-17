import ctypes, sys

class VkDeviceGroupSwapchainCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('modes', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDeviceGroupSwapchainCreateInfoKHR
