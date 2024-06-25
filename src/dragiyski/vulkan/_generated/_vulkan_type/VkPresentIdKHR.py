import ctypes

class VkPresentIdKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchainCount', ctypes.c_uint32),
        ('pPresentIds', ctypes.POINTER(ctypes.c_uint64)),
    ]

VkPresentIdKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'swapchainCount': ctypes.c_uint32,
    'pPresentIds': ctypes.POINTER(ctypes.c_uint64),
}
