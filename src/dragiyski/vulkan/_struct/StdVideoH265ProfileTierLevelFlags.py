import ctypes, sys

class StdVideoH265ProfileTierLevelFlags(ctypes.Structure):
    _fields_ = [
        ('general_tier_flag', ctypes.c_uint32, 1),
        ('general_progressive_source_flag', ctypes.c_uint32, 1),
        ('general_interlaced_source_flag', ctypes.c_uint32, 1),
        ('general_non_packed_constraint_flag', ctypes.c_uint32, 1),
        ('general_frame_only_constraint_flag', ctypes.c_uint32, 1),
    ]

sys.modules[__name__] = StdVideoH265ProfileTierLevelFlags