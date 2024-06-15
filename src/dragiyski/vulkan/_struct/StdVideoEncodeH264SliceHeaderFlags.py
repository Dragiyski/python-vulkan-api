import ctypes, sys

class StdVideoEncodeH264SliceHeaderFlags(ctypes.Structure):
    _fields_ = [
        ('direct_spatial_mv_pred_flag', ctypes.c_uint32, 1),
        ('num_ref_idx_active_override_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

sys.modules[__name__] = StdVideoEncodeH264SliceHeaderFlags
