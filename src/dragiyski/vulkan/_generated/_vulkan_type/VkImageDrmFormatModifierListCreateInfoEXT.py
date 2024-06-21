import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('drmFormatModifierCount', ctypes.c_uint32),
        ('pDrmFormatModifiers', ctypes.POINTER(ctypes.c_uint64)),
    ]
