import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('enableYDegamma', ctypes.c_uint32),
        ('enableCbCrDegamma', ctypes.c_uint32),
    ]
