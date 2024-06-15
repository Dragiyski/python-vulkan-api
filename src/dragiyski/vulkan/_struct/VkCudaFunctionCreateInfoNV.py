import ctypes, sys

class VkCudaFunctionCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('module', ctypes.c_void_p),
        ('pName', ctypes.c_char_p),
    ]

sys.modules[__name__] = VkCudaFunctionCreateInfoNV
