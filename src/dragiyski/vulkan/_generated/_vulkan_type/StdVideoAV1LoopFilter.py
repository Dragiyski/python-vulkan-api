import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1LoopFilterFlags import CType as StdVideoAV1LoopFilterFlags

CType._fields_ = [
    ('flags', StdVideoAV1LoopFilterFlags),
    ('loop_filter_level', ctypes.ARRAY(ctypes.c_uint8, 4)),
    ('loop_filter_sharpness', ctypes.c_uint8),
    ('update_ref_delta', ctypes.c_uint8),
    ('loop_filter_ref_deltas', ctypes.ARRAY(ctypes.c_int8, 8)),
    ('update_mode_delta', ctypes.c_uint8),
    ('loop_filter_mode_deltas', ctypes.ARRAY(ctypes.c_int8, 2)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoAV1LoopFilterFlags',
    },
    'included_in': {
        'StdVideoDecodeAV1PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoAV1LoopFilterFlags'},
        'loop_filter_level': {'python_name': ['loop', 'filter', 'level']},
        'loop_filter_sharpness': {'python_name': ['loop', 'filter', 'sharpness']},
        'update_ref_delta': {'python_name': ['update', 'ref', 'delta']},
        'loop_filter_ref_deltas': {'python_name': ['loop', 'filter', 'ref', 'deltas']},
        'update_mode_delta': {'python_name': ['update', 'mode', 'delta']},
        'loop_filter_mode_deltas': {'python_name': ['loop', 'filter', 'mode', 'deltas']},
    }
}
