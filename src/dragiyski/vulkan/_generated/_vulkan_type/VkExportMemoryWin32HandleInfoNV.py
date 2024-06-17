import ctypes, sys

class VkExportMemoryWin32HandleInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pAttributes', ctypes.c_void_p),
        ('dwAccess', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkExportMemoryWin32HandleInfoNV
