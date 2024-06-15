import ctypes, sys

class VkMemoryGetSciBufInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMemoryGetSciBufInfoNV
