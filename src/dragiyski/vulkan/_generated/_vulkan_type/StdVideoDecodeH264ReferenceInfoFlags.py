import ctypes

class StdVideoDecodeH264ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('top_field_flag', ctypes.c_uint32, 1),
        ('bottom_field_flag', ctypes.c_uint32, 1),
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('is_non_existing', ctypes.c_uint32, 1),
    ]

StdVideoDecodeH264ReferenceInfoFlags._type_ = {
    'top_field_flag': ctypes.c_uint32,
    'bottom_field_flag': ctypes.c_uint32,
    'used_for_long_term_reference': ctypes.c_uint32,
    'is_non_existing': ctypes.c_uint32,
}
