import ctypes, sys

class VkExportMemoryAllocateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleTypes', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkExportMemoryAllocateInfoNV
