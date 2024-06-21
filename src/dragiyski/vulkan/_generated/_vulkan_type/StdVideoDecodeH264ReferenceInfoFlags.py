import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('top_field_flag', ctypes.c_uint32, 1),
        ('bottom_field_flag', ctypes.c_uint32, 1),
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('is_non_existing', ctypes.c_uint32, 1),
    ]
