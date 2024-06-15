import ctypes, sys

class VkImportMemoryFdInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('fd', ctypes.c_int),
    ]

sys.modules[__name__] = VkImportMemoryFdInfoKHR
