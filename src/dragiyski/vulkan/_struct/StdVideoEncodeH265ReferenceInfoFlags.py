import ctypes, sys

class StdVideoEncodeH265ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('unused_for_reference', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

sys.modules[__name__] = StdVideoEncodeH265ReferenceInfoFlags
