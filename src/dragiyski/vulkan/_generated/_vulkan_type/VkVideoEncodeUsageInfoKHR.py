import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoUsageHints', ctypes.c_uint32),
        ('videoContentHints', ctypes.c_uint32),
        ('tuningMode', ctypes.c_int),
    ]
