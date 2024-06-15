import ctypes, sys

class VkPresentIdKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchainCount', ctypes.c_uint32),
        ('pPresentIds', ctypes.POINTER(ctypes.c_uint64)),
    ]

sys.modules[__name__] = VkPresentIdKHR
