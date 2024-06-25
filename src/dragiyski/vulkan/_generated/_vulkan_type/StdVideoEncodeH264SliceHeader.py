import ctypes

class StdVideoEncodeH264SliceHeader(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoEncodeH264SliceHeaderFlags,
            'first_mb_in_slice': ctypes.c_uint32,
            'slice_type': ctypes.c_int,
            'slice_alpha_c0_offset_div2': ctypes.c_int8,
            'slice_beta_offset_div2': ctypes.c_int8,
            'slice_qp_delta': ctypes.c_int8,
            'reserved1': ctypes.c_uint8,
            'cabac_init_idc': ctypes.c_int,
            'disable_deblocking_filter_idc': ctypes.c_int,
            'pWeightTable': ctypes.POINTER(StdVideoEncodeH264WeightTable),
        }


from .StdVideoEncodeH264SliceHeaderFlags import StdVideoEncodeH264SliceHeaderFlags
from .StdVideoEncodeH264WeightTable import StdVideoEncodeH264WeightTable

StdVideoEncodeH264SliceHeader._fields_ = [
    ('flags', StdVideoEncodeH264SliceHeaderFlags),
    ('first_mb_in_slice', ctypes.c_uint32),
    ('slice_type', ctypes.c_int),
    ('slice_alpha_c0_offset_div2', ctypes.c_int8),
    ('slice_beta_offset_div2', ctypes.c_int8),
    ('slice_qp_delta', ctypes.c_int8),
    ('reserved1', ctypes.c_uint8),
    ('cabac_init_idc', ctypes.c_int),
    ('disable_deblocking_filter_idc', ctypes.c_int),
    ('pWeightTable', ctypes.POINTER(StdVideoEncodeH264WeightTable)),
]
