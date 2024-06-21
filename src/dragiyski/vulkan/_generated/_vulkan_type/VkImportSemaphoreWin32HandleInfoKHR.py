import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_void_p),
        ('name', ctypes.c_wchar_p),
    ]
