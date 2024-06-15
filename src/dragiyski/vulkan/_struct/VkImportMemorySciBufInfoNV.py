import ctypes, sys

class VkImportMemorySciBufInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkImportMemorySciBufInfoNV
