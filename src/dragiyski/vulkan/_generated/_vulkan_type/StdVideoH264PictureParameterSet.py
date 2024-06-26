import ctypes

class StdVideoH264PictureParameterSet(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH264PpsFlags',
        'StdVideoH264ScalingLists',
    }
    _included_in_ = {
        'VkVideoDecodeH264SessionParametersAddInfoKHR',
        'VkVideoEncodeH264SessionParametersAddInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'seq_parameter_set_id': 'seq_parameter_set_id',
        'pic_parameter_set_id': 'pic_parameter_set_id',
        'num_ref_idx_l0_default_active_minus1': 'num_ref_idx_l0_default_active_minus1',
        'num_ref_idx_l1_default_active_minus1': 'num_ref_idx_l1_default_active_minus1',
        'weighted_bipred_idc': 'weighted_bipred_idc',
        'pic_init_qp_minus26': 'pic_init_qp_minus26',
        'pic_init_qs_minus26': 'pic_init_qs_minus26',
        'chroma_qp_index_offset': 'chroma_qp_index_offset',
        'second_chroma_qp_index_offset': 'second_chroma_qp_index_offset',
        'pScalingLists': 'scaling_lists',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std',
    }
    _vk_enum_ = {
        'weighted_bipred_idc': 'StdVideoH264WeightedBipredIdc',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoH264PpsFlags import StdVideoH264PpsFlags
from .StdVideoH264ScalingLists import StdVideoH264ScalingLists

StdVideoH264PictureParameterSet._fields_ = [
    ('flags', StdVideoH264PpsFlags),
    ('seq_parameter_set_id', ctypes.c_uint8),
    ('pic_parameter_set_id', ctypes.c_uint8),
    ('num_ref_idx_l0_default_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_default_active_minus1', ctypes.c_uint8),
    ('weighted_bipred_idc', ctypes.c_int),
    ('pic_init_qp_minus26', ctypes.c_int8),
    ('pic_init_qs_minus26', ctypes.c_int8),
    ('chroma_qp_index_offset', ctypes.c_int8),
    ('second_chroma_qp_index_offset', ctypes.c_int8),
    ('pScalingLists', ctypes.POINTER(StdVideoH264ScalingLists)),
]

StdVideoH264PictureParameterSet._type_ = {
    'flags': StdVideoH264PpsFlags,
    'seq_parameter_set_id': ctypes.c_uint8,
    'pic_parameter_set_id': ctypes.c_uint8,
    'num_ref_idx_l0_default_active_minus1': ctypes.c_uint8,
    'num_ref_idx_l1_default_active_minus1': ctypes.c_uint8,
    'weighted_bipred_idc': ctypes.c_int,
    'pic_init_qp_minus26': ctypes.c_int8,
    'pic_init_qs_minus26': ctypes.c_int8,
    'chroma_qp_index_offset': ctypes.c_int8,
    'second_chroma_qp_index_offset': ctypes.c_int8,
    'pScalingLists': ctypes.POINTER(StdVideoH264ScalingLists),
}
