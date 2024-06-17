import ctypes, sys

class VkSysmemColorSpaceFUCHSIA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorSpace', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSysmemColorSpaceFUCHSIA
