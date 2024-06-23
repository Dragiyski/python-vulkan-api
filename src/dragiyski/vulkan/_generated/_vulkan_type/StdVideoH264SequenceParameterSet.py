import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH264ScalingLists import CType as StdVideoH264ScalingLists
from .StdVideoH264SequenceParameterSetVui import CType as StdVideoH264SequenceParameterSetVui
from .StdVideoH264SpsFlags import CType as StdVideoH264SpsFlags

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoH264ScalingLists',
        'StdVideoH264SequenceParameterSetVui',
        'StdVideoH264SpsFlags',
    },
    'included_in': {
        'VkVideoDecodeH264SessionParametersAddInfoKHR',
        'VkVideoEncodeH264SessionParametersAddInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoH264SpsFlags'},
        'profile_idc': {'python_name': ['profile', 'idc'], 'type': 'StdVideoH264ProfileIdc'},
        'level_idc': {'python_name': ['level', 'idc'], 'type': 'StdVideoH264LevelIdc'},
        'chroma_format_idc': {'python_name': ['chroma', 'format', 'idc'], 'type': 'StdVideoH264ChromaFormatIdc'},
        'seq_parameter_set_id': {'python_name': ['seq', 'parameter', 'set', 'id']},
        'bit_depth_luma_minus8': {'python_name': ['bit', 'depth', 'luma', 'minus8']},
        'bit_depth_chroma_minus8': {'python_name': ['bit', 'depth', 'chroma', 'minus8']},
        'log2_max_frame_num_minus4': {'python_name': ['log2', 'max', 'frame', 'num', 'minus4']},
        'pic_order_cnt_type': {'python_name': ['pic', 'order', 'cnt', 'type'], 'type': 'StdVideoH264PocType'},
        'offset_for_non_ref_pic': {'python_name': ['offset', 'for', 'non', 'ref', 'pic']},
        'offset_for_top_to_bottom_field': {'python_name': ['offset', 'for', 'top', 'to', 'bottom', 'field']},
        'log2_max_pic_order_cnt_lsb_minus4': {'python_name': ['log2', 'max', 'pic', 'order', 'cnt', 'lsb', 'minus4']},
        'num_ref_frames_in_pic_order_cnt_cycle': {'python_name': ['num', 'ref', 'frames', 'in', 'pic', 'order', 'cnt', 'cycle']},
        'max_num_ref_frames': {'python_name': ['max', 'num', 'ref', 'frames']},
        'reserved1': {'python_name': ['reserved1']},
        'pic_width_in_mbs_minus1': {'python_name': ['pic', 'width', 'in', 'mbs', 'minus1']},
        'pic_height_in_map_units_minus1': {'python_name': ['pic', 'height', 'in', 'map', 'units', 'minus1']},
        'frame_crop_left_offset': {'python_name': ['frame', 'crop', 'left', 'offset']},
        'frame_crop_right_offset': {'python_name': ['frame', 'crop', 'right', 'offset']},
        'frame_crop_top_offset': {'python_name': ['frame', 'crop', 'top', 'offset']},
        'frame_crop_bottom_offset': {'python_name': ['frame', 'crop', 'bottom', 'offset']},
        'reserved2': {'python_name': ['reserved2']},
        'pOffsetForRefFrame': {'python_name': ['p', 'offset', 'for', 'ref', 'frame']},
        'pScalingLists': {'python_name': ['p', 'scaling', 'lists'], 'type': 'StdVideoH264ScalingLists'},
        'pSequenceParameterSetVui': {'python_name': ['p', 'sequence', 'parameter', 'set', 'vui'], 'type': 'StdVideoH264SequenceParameterSetVui'},
    }
}
