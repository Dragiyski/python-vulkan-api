import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('lowLatencyMode', ctypes.c_uint32),
        ('lowLatencyBoost', ctypes.c_uint32),
        ('minimumIntervalUs', ctypes.c_uint32),
    ]
