import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('loop_filter_delta_enabled', ctypes.c_uint32, 1),
        ('loop_filter_delta_update', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]
