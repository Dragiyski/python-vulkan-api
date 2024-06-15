import ctypes, sys

class VkCudaModuleCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dataSize', ctypes.c_size_t),
        ('pData', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkCudaModuleCreateInfoNV
