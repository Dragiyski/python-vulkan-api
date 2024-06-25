import ctypes

class StdVideoEncodeH264SliceHeaderFlags(ctypes.Structure):
    _fields_ = [
        ('direct_spatial_mv_pred_flag', ctypes.c_uint32, 1),
        ('num_ref_idx_active_override_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

StdVideoEncodeH264SliceHeaderFlags._type_ = {
    'direct_spatial_mv_pred_flag': ctypes.c_uint32,
    'num_ref_idx_active_override_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
