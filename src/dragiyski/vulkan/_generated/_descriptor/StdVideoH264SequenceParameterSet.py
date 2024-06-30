from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH264SequenceParameterSet'
_member_list_ = ['flags', 'profile_idc', 'level_idc', 'chroma_format_idc', 'seq_parameter_set_id', 'bit_depth_luma_minus8', 'bit_depth_chroma_minus8', 'log2_max_frame_num_minus4', 'pic_order_cnt_type', 'offset_for_non_ref_pic', 'offset_for_top_to_bottom_field', 'log2_max_pic_order_cnt_lsb_minus4', 'num_ref_frames_in_pic_order_cnt_cycle', 'max_num_ref_frames', 'reserved1', 'pic_width_in_mbs_minus1', 'pic_height_in_map_units_minus1', 'frame_crop_left_offset', 'frame_crop_right_offset', 'frame_crop_top_offset', 'frame_crop_bottom_offset', 'reserved2', 'pOffsetForRefFrame', 'pScalingLists', 'pSequenceParameterSetVui']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH264SpsFlags'),
        'type_name': 'StdVideoH264SpsFlags',
        'structure': 'StdVideoH264SpsFlags',
        'is_string': False,
    },
    'profile_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264ProfileIdc',
        'enum': 'StdVideoH264ProfileIdc',
        'is_string': False,
    },
    'level_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264LevelIdc',
        'enum': 'StdVideoH264LevelIdc',
        'is_string': False,
    },
    'chroma_format_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264ChromaFormatIdc',
        'enum': 'StdVideoH264ChromaFormatIdc',
        'is_string': False,
    },
    'seq_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'bit_depth_luma_minus8': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'bit_depth_chroma_minus8': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_max_frame_num_minus4': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pic_order_cnt_type': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264PocType',
        'enum': 'StdVideoH264PocType',
        'is_string': False,
    },
    'offset_for_non_ref_pic': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'offset_for_top_to_bottom_field': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'log2_max_pic_order_cnt_lsb_minus4': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_ref_frames_in_pic_order_cnt_cycle': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'max_num_ref_frames': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pic_width_in_mbs_minus1': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pic_height_in_map_units_minus1': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'frame_crop_left_offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'frame_crop_right_offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'frame_crop_top_offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'frame_crop_bottom_offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'reserved2': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pOffsetForRefFrame': {
        'type': CPointerType(CIntType('c_int32')),
        'is_string': False,
    },
    'pScalingLists': {
        'type': CPointerType(CComplexType('StdVideoH264ScalingLists')),
        'type_name': 'StdVideoH264ScalingLists',
        'structure': 'StdVideoH264ScalingLists',
        'is_string': False,
    },
    'pSequenceParameterSetVui': {
        'type': CPointerType(CComplexType('StdVideoH264SequenceParameterSetVui')),
        'type_name': 'StdVideoH264SequenceParameterSetVui',
        'structure': 'StdVideoH264SequenceParameterSetVui',
        'is_string': False,
    },
}
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
