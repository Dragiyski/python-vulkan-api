import ctypes, sys

class VkSubpassBeginInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('contents', ctypes.c_int),
    ]

sys.modules[__name__] = VkSubpassBeginInfo
