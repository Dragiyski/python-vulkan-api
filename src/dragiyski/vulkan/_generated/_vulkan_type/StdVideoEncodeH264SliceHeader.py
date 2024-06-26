import ctypes

class StdVideoEncodeH264SliceHeader(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH264SliceHeaderFlags',
        'StdVideoEncodeH264WeightTable',
    }
    _included_in_ = {
        'VkVideoEncodeH264NaluSliceInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'first_mb_in_slice': 'first_mb_in_slice',
        'slice_type': 'slice_type',
        'slice_alpha_c0_offset_div2': 'slice_alpha_c0_offset_div2',
        'slice_beta_offset_div2': 'slice_beta_offset_div2',
        'slice_qp_delta': 'slice_qp_delta',
        'reserved1': 'reserved1',
        'cabac_init_idc': 'cabac_init_idc',
        'disable_deblocking_filter_idc': 'disable_deblocking_filter_idc',
        'pWeightTable': 'weight_table',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std_encode',
    }
    _vk_enum_ = {
        'slice_type': 'StdVideoH264SliceType',
        'cabac_init_idc': 'StdVideoH264CabacInitIdc',
        'disable_deblocking_filter_idc': 'StdVideoH264DisableDeblockingFilterIdc',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


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

StdVideoEncodeH264SliceHeader._type_ = {
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
