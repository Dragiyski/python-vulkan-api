import ctypes, sys

class VkImageSwapchainCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchain', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkImageSwapchainCreateInfoKHR
