import ctypes, sys

class StdVideoDecodeH264ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('top_field_flag', ctypes.c_uint32, 1),
        ('bottom_field_flag', ctypes.c_uint32, 1),
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('is_non_existing', ctypes.c_uint32, 1),
    ]

sys.modules[__name__] = StdVideoDecodeH264ReferenceInfoFlags
