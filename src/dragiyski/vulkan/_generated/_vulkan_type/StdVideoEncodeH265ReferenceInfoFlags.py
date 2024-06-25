import ctypes

class StdVideoEncodeH265ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('unused_for_reference', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

StdVideoEncodeH265ReferenceInfoFlags._type_ = {
    'used_for_long_term_reference': ctypes.c_uint32,
    'unused_for_reference': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
