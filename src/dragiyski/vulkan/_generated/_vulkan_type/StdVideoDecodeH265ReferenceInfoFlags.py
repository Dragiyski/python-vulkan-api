import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('unused_for_reference', ctypes.c_uint32, 1),
    ]
