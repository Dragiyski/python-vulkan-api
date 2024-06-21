import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('cdef_damping_minus_3', ctypes.c_uint8),
        ('cdef_bits', ctypes.c_uint8),
        ('cdef_y_pri_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_y_sec_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_uv_pri_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_uv_sec_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
    ]
