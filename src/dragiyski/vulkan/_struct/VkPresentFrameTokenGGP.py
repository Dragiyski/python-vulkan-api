import ctypes, sys

class VkPresentFrameTokenGGP(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('frameToken', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPresentFrameTokenGGP
