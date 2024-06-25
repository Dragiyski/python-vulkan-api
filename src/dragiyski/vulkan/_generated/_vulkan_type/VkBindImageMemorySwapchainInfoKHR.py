import ctypes

class VkBindImageMemorySwapchainInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchain', ctypes.c_void_p),
        ('imageIndex', ctypes.c_uint32),
    ]

VkBindImageMemorySwapchainInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'swapchain': ctypes.c_void_p,
    'imageIndex': ctypes.c_uint32,
}
