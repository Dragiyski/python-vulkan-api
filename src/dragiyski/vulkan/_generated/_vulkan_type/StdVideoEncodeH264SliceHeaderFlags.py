import ctypes

class StdVideoEncodeH264SliceHeaderFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'direct_spatial_mv_pred_flag': ctypes.c_uint32,
            'num_ref_idx_active_override_flag': ctypes.c_uint32,
            'reserved': ctypes.c_uint32,
        }

    _fields_ = [
        ('direct_spatial_mv_pred_flag', ctypes.c_uint32, 1),
        ('num_ref_idx_active_override_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]
