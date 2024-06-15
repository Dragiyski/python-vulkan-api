import ctypes, sys

class VkExportFenceSciSyncInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pAttributes', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkExportFenceSciSyncInfoNV
