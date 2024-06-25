import ctypes

class VkSwapchainPresentFenceInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchainCount', ctypes.c_uint32),
        ('pFences', ctypes.POINTER(ctypes.c_void_p)),
    ]

VkSwapchainPresentFenceInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'swapchainCount': ctypes.c_uint32,
    'pFences': ctypes.POINTER(ctypes.c_void_p),
}
