import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH265DecPicBufMgr import CType as StdVideoH265DecPicBufMgr
from .StdVideoH265LongTermRefPicsSps import CType as StdVideoH265LongTermRefPicsSps
from .StdVideoH265PredictorPaletteEntries import CType as StdVideoH265PredictorPaletteEntries
from .StdVideoH265ProfileTierLevel import CType as StdVideoH265ProfileTierLevel
from .StdVideoH265ScalingLists import CType as StdVideoH265ScalingLists
from .StdVideoH265SequenceParameterSetVui import CType as StdVideoH265SequenceParameterSetVui
from .StdVideoH265ShortTermRefPicSet import CType as StdVideoH265ShortTermRefPicSet
from .StdVideoH265SpsFlags import CType as StdVideoH265SpsFlags

CType._fields_ = [
    ('flags', StdVideoH265SpsFlags),
    ('chroma_format_idc', ctypes.c_int),
    ('pic_width_in_luma_samples', ctypes.c_uint32),
    ('pic_height_in_luma_samples', ctypes.c_uint32),
    ('sps_video_parameter_set_id', ctypes.c_uint8),
    ('sps_max_sub_layers_minus1', ctypes.c_uint8),
    ('sps_seq_parameter_set_id', ctypes.c_uint8),
    ('bit_depth_luma_minus8', ctypes.c_uint8),
    ('bit_depth_chroma_minus8', ctypes.c_uint8),
    ('log2_max_pic_order_cnt_lsb_minus4', ctypes.c_uint8),
    ('log2_min_luma_coding_block_size_minus3', ctypes.c_uint8),
    ('log2_diff_max_min_luma_coding_block_size', ctypes.c_uint8),
    ('log2_min_luma_transform_block_size_minus2', ctypes.c_uint8),
    ('log2_diff_max_min_luma_transform_block_size', ctypes.c_uint8),
    ('max_transform_hierarchy_depth_inter', ctypes.c_uint8),
    ('max_transform_hierarchy_depth_intra', ctypes.c_uint8),
    ('num_short_term_ref_pic_sets', ctypes.c_uint8),
    ('num_long_term_ref_pics_sps', ctypes.c_uint8),
    ('pcm_sample_bit_depth_luma_minus1', ctypes.c_uint8),
    ('pcm_sample_bit_depth_chroma_minus1', ctypes.c_uint8),
    ('log2_min_pcm_luma_coding_block_size_minus3', ctypes.c_uint8),
    ('log2_diff_max_min_pcm_luma_coding_block_size', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('reserved2', ctypes.c_uint8),
    ('palette_max_size', ctypes.c_uint8),
    ('delta_palette_max_predictor_size', ctypes.c_uint8),
    ('motion_vector_resolution_control_idc', ctypes.c_uint8),
    ('sps_num_palette_predictor_initializers_minus1', ctypes.c_uint8),
    ('conf_win_left_offset', ctypes.c_uint32),
    ('conf_win_right_offset', ctypes.c_uint32),
    ('conf_win_top_offset', ctypes.c_uint32),
    ('conf_win_bottom_offset', ctypes.c_uint32),
    ('pProfileTierLevel', ctypes.POINTER(StdVideoH265ProfileTierLevel)),
    ('pDecPicBufMgr', ctypes.POINTER(StdVideoH265DecPicBufMgr)),
    ('pScalingLists', ctypes.POINTER(StdVideoH265ScalingLists)),
    ('pShortTermRefPicSet', ctypes.POINTER(StdVideoH265ShortTermRefPicSet)),
    ('pLongTermRefPicsSps', ctypes.POINTER(StdVideoH265LongTermRefPicsSps)),
    ('pSequenceParameterSetVui', ctypes.POINTER(StdVideoH265SequenceParameterSetVui)),
    ('pPredictorPaletteEntries', ctypes.POINTER(StdVideoH265PredictorPaletteEntries)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoH265DecPicBufMgr',
        'StdVideoH265LongTermRefPicsSps',
        'StdVideoH265PredictorPaletteEntries',
        'StdVideoH265ProfileTierLevel',
        'StdVideoH265ScalingLists',
        'StdVideoH265SequenceParameterSetVui',
        'StdVideoH265ShortTermRefPicSet',
        'StdVideoH265SpsFlags',
    },
    'included_in': {
        'VkVideoDecodeH265SessionParametersAddInfoKHR',
        'VkVideoEncodeH265SessionParametersAddInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoH265SpsFlags'},
        'chroma_format_idc': {'python_name': ['chroma', 'format', 'idc'], 'type': 'StdVideoH265ChromaFormatIdc'},
        'pic_width_in_luma_samples': {'python_name': ['pic', 'width', 'in', 'luma', 'samples']},
        'pic_height_in_luma_samples': {'python_name': ['pic', 'height', 'in', 'luma', 'samples']},
        'sps_video_parameter_set_id': {'python_name': ['sps', 'video', 'parameter', 'set', 'id']},
        'sps_max_sub_layers_minus1': {'python_name': ['sps', 'max', 'sub', 'layers', 'minus1']},
        'sps_seq_parameter_set_id': {'python_name': ['sps', 'seq', 'parameter', 'set', 'id']},
        'bit_depth_luma_minus8': {'python_name': ['bit', 'depth', 'luma', 'minus8']},
        'bit_depth_chroma_minus8': {'python_name': ['bit', 'depth', 'chroma', 'minus8']},
        'log2_max_pic_order_cnt_lsb_minus4': {'python_name': ['log2', 'max', 'pic', 'order', 'cnt', 'lsb', 'minus4']},
        'log2_min_luma_coding_block_size_minus3': {'python_name': ['log2', 'min', 'luma', 'coding', 'block', 'size', 'minus3']},
        'log2_diff_max_min_luma_coding_block_size': {'python_name': ['log2', 'diff', 'max', 'min', 'luma', 'coding', 'block', 'size']},
        'log2_min_luma_transform_block_size_minus2': {'python_name': ['log2', 'min', 'luma', 'transform', 'block', 'size', 'minus2']},
        'log2_diff_max_min_luma_transform_block_size': {'python_name': ['log2', 'diff', 'max', 'min', 'luma', 'transform', 'block', 'size']},
        'max_transform_hierarchy_depth_inter': {'python_name': ['max', 'transform', 'hierarchy', 'depth', 'inter']},
        'max_transform_hierarchy_depth_intra': {'python_name': ['max', 'transform', 'hierarchy', 'depth', 'intra']},
        'num_short_term_ref_pic_sets': {'python_name': ['num', 'short', 'term', 'ref', 'pic', 'sets']},
        'num_long_term_ref_pics_sps': {'python_name': ['num', 'long', 'term', 'ref', 'pics', 'sps']},
        'pcm_sample_bit_depth_luma_minus1': {'python_name': ['pcm', 'sample', 'bit', 'depth', 'luma', 'minus1']},
        'pcm_sample_bit_depth_chroma_minus1': {'python_name': ['pcm', 'sample', 'bit', 'depth', 'chroma', 'minus1']},
        'log2_min_pcm_luma_coding_block_size_minus3': {'python_name': ['log2', 'min', 'pcm', 'luma', 'coding', 'block', 'size', 'minus3']},
        'log2_diff_max_min_pcm_luma_coding_block_size': {'python_name': ['log2', 'diff', 'max', 'min', 'pcm', 'luma', 'coding', 'block', 'size']},
        'reserved1': {'python_name': ['reserved1']},
        'reserved2': {'python_name': ['reserved2']},
        'palette_max_size': {'python_name': ['palette', 'max', 'size']},
        'delta_palette_max_predictor_size': {'python_name': ['delta', 'palette', 'max', 'predictor', 'size']},
        'motion_vector_resolution_control_idc': {'python_name': ['motion', 'vector', 'resolution', 'control', 'idc']},
        'sps_num_palette_predictor_initializers_minus1': {'python_name': ['sps', 'num', 'palette', 'predictor', 'initializers', 'minus1']},
        'conf_win_left_offset': {'python_name': ['conf', 'win', 'left', 'offset']},
        'conf_win_right_offset': {'python_name': ['conf', 'win', 'right', 'offset']},
        'conf_win_top_offset': {'python_name': ['conf', 'win', 'top', 'offset']},
        'conf_win_bottom_offset': {'python_name': ['conf', 'win', 'bottom', 'offset']},
        'pProfileTierLevel': {'python_name': ['p', 'profile', 'tier', 'level'], 'type': 'StdVideoH265ProfileTierLevel'},
        'pDecPicBufMgr': {'python_name': ['p', 'dec', 'pic', 'buf', 'mgr'], 'type': 'StdVideoH265DecPicBufMgr'},
        'pScalingLists': {'python_name': ['p', 'scaling', 'lists'], 'type': 'StdVideoH265ScalingLists'},
        'pShortTermRefPicSet': {'python_name': ['p', 'short', 'term', 'ref', 'pic', 'set'], 'type': 'StdVideoH265ShortTermRefPicSet'},
        'pLongTermRefPicsSps': {'python_name': ['p', 'long', 'term', 'ref', 'pics', 'sps'], 'type': 'StdVideoH265LongTermRefPicsSps'},
        'pSequenceParameterSetVui': {'python_name': ['p', 'sequence', 'parameter', 'set', 'vui'], 'type': 'StdVideoH265SequenceParameterSetVui'},
        'pPredictorPaletteEntries': {'python_name': ['p', 'predictor', 'palette', 'entries'], 'type': 'StdVideoH265PredictorPaletteEntries'},
    }
}
