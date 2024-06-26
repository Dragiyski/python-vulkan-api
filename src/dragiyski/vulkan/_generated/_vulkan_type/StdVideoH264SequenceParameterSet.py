import ctypes

class StdVideoH264SequenceParameterSet(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH264ScalingLists',
        'StdVideoH264SequenceParameterSetVui',
        'StdVideoH264SpsFlags',
    }
    _included_in_ = {
        'VkVideoDecodeH264SessionParametersAddInfoKHR',
        'VkVideoEncodeH264SessionParametersAddInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'profile_idc': 'profile_idc',
        'level_idc': 'level_idc',
        'chroma_format_idc': 'chroma_format_idc',
        'seq_parameter_set_id': 'seq_parameter_set_id',
        'bit_depth_luma_minus8': 'bit_depth_luma_minus8',
        'bit_depth_chroma_minus8': 'bit_depth_chroma_minus8',
        'log2_max_frame_num_minus4': 'log2_max_frame_num_minus4',
        'pic_order_cnt_type': 'pic_order_cnt_type',
        'offset_for_non_ref_pic': 'offset_for_non_ref_pic',
        'offset_for_top_to_bottom_field': 'offset_for_top_to_bottom_field',
        'log2_max_pic_order_cnt_lsb_minus4': 'log2_max_pic_order_cnt_lsb_minus4',
        'num_ref_frames_in_pic_order_cnt_cycle': 'num_ref_frames_in_pic_order_cnt_cycle',
        'max_num_ref_frames': 'max_num_ref_frames',
        'reserved1': 'reserved1',
        'pic_width_in_mbs_minus1': 'pic_width_in_mbs_minus1',
        'pic_height_in_map_units_minus1': 'pic_height_in_map_units_minus1',
        'frame_crop_left_offset': 'frame_crop_left_offset',
        'frame_crop_right_offset': 'frame_crop_right_offset',
        'frame_crop_top_offset': 'frame_crop_top_offset',
        'frame_crop_bottom_offset': 'frame_crop_bottom_offset',
        'reserved2': 'reserved2',
        'pOffsetForRefFrame': 'offset_for_ref_frame',
        'pScalingLists': 'scaling_lists',
        'pSequenceParameterSetVui': 'sequence_parameter_set_vui',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std',
    }
    _vk_enum_ = {
        'profile_idc': 'StdVideoH264ProfileIdc',
        'level_idc': 'StdVideoH264LevelIdc',
        'chroma_format_idc': 'StdVideoH264ChromaFormatIdc',
        'pic_order_cnt_type': 'StdVideoH264PocType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoH264ScalingLists import StdVideoH264ScalingLists
from .StdVideoH264SequenceParameterSetVui import StdVideoH264SequenceParameterSetVui
from .StdVideoH264SpsFlags import StdVideoH264SpsFlags

StdVideoH264SequenceParameterSet._fields_ = [
    ('flags', StdVideoH264SpsFlags),
    ('profile_idc', ctypes.c_int),
    ('level_idc', ctypes.c_int),
    ('chroma_format_idc', ctypes.c_int),
    ('seq_parameter_set_id', ctypes.c_uint8),
    ('bit_depth_luma_minus8', ctypes.c_uint8),
    ('bit_depth_chroma_minus8', ctypes.c_uint8),
    ('log2_max_frame_num_minus4', ctypes.c_uint8),
    ('pic_order_cnt_type', ctypes.c_int),
    ('offset_for_non_ref_pic', ctypes.c_int32),
    ('offset_for_top_to_bottom_field', ctypes.c_int32),
    ('log2_max_pic_order_cnt_lsb_minus4', ctypes.c_uint8),
    ('num_ref_frames_in_pic_order_cnt_cycle', ctypes.c_uint8),
    ('max_num_ref_frames', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('pic_width_in_mbs_minus1', ctypes.c_uint32),
    ('pic_height_in_map_units_minus1', ctypes.c_uint32),
    ('frame_crop_left_offset', ctypes.c_uint32),
    ('frame_crop_right_offset', ctypes.c_uint32),
    ('frame_crop_top_offset', ctypes.c_uint32),
    ('frame_crop_bottom_offset', ctypes.c_uint32),
    ('reserved2', ctypes.c_uint32),
    ('pOffsetForRefFrame', ctypes.POINTER(ctypes.c_int32)),
    ('pScalingLists', ctypes.POINTER(StdVideoH264ScalingLists)),
    ('pSequenceParameterSetVui', ctypes.POINTER(StdVideoH264SequenceParameterSetVui)),
]

StdVideoH264SequenceParameterSet._type_ = {
    'flags': StdVideoH264SpsFlags,
    'profile_idc': ctypes.c_int,
    'level_idc': ctypes.c_int,
    'chroma_format_idc': ctypes.c_int,
    'seq_parameter_set_id': ctypes.c_uint8,
    'bit_depth_luma_minus8': ctypes.c_uint8,
    'bit_depth_chroma_minus8': ctypes.c_uint8,
    'log2_max_frame_num_minus4': ctypes.c_uint8,
    'pic_order_cnt_type': ctypes.c_int,
    'offset_for_non_ref_pic': ctypes.c_int32,
    'offset_for_top_to_bottom_field': ctypes.c_int32,
    'log2_max_pic_order_cnt_lsb_minus4': ctypes.c_uint8,
    'num_ref_frames_in_pic_order_cnt_cycle': ctypes.c_uint8,
    'max_num_ref_frames': ctypes.c_uint8,
    'reserved1': ctypes.c_uint8,
    'pic_width_in_mbs_minus1': ctypes.c_uint32,
    'pic_height_in_map_units_minus1': ctypes.c_uint32,
    'frame_crop_left_offset': ctypes.c_uint32,
    'frame_crop_right_offset': ctypes.c_uint32,
    'frame_crop_top_offset': ctypes.c_uint32,
    'frame_crop_bottom_offset': ctypes.c_uint32,
    'reserved2': ctypes.c_uint32,
    'pOffsetForRefFrame': ctypes.POINTER(ctypes.c_int32),
    'pScalingLists': ctypes.POINTER(StdVideoH264ScalingLists),
    'pSequenceParameterSetVui': ctypes.POINTER(StdVideoH264SequenceParameterSetVui),
}
