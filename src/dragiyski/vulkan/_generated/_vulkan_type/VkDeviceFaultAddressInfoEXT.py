import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('addressType', ctypes.c_int),
        ('reportedAddress', ctypes.c_uint64),
        ('addressPrecision', ctypes.c_uint64),
    ]
