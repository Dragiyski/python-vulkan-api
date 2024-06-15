import ctypes, sys

class StdVideoDecodeH265ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('unused_for_reference', ctypes.c_uint32, 1),
    ]

sys.modules[__name__] = StdVideoDecodeH265ReferenceInfoFlags
