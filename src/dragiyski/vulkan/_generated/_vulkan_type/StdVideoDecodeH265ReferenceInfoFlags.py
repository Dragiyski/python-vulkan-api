import ctypes

class StdVideoDecodeH265ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('unused_for_reference', ctypes.c_uint32, 1),
    ]

StdVideoDecodeH265ReferenceInfoFlags._type_ = {
    'used_for_long_term_reference': ctypes.c_uint32,
    'unused_for_reference': ctypes.c_uint32,
}
