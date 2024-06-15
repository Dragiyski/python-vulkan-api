import ctypes, sys

class StdVideoEncodeH264ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

sys.modules[__name__] = StdVideoEncodeH264ReferenceInfoFlags
