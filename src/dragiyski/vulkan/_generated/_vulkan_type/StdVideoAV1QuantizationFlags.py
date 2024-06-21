import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('using_qmatrix', ctypes.c_uint32, 1),
        ('diff_uv_delta', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]
