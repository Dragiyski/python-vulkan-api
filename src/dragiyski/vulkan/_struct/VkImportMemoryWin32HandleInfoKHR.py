import ctypes, sys

class VkImportMemoryWin32HandleInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_void_p),
        ('name', ctypes.c_wchar_p),
    ]

sys.modules[__name__] = VkImportMemoryWin32HandleInfoKHR
