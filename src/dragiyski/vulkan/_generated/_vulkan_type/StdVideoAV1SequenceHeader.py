import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1ColorConfig import CType as StdVideoAV1ColorConfig
from .StdVideoAV1SequenceHeaderFlags import CType as StdVideoAV1SequenceHeaderFlags
from .StdVideoAV1TimingInfo import CType as StdVideoAV1TimingInfo

CType._fields_ = [
    ('flags', StdVideoAV1SequenceHeaderFlags),
    ('seq_profile', ctypes.c_int),
    ('frame_width_bits_minus_1', ctypes.c_uint8),
    ('frame_height_bits_minus_1', ctypes.c_uint8),
    ('max_frame_width_minus_1', ctypes.c_uint16),
    ('max_frame_height_minus_1', ctypes.c_uint16),
    ('delta_frame_id_length_minus_2', ctypes.c_uint8),
    ('additional_frame_id_length_minus_1', ctypes.c_uint8),
    ('order_hint_bits_minus_1', ctypes.c_uint8),
    ('seq_force_integer_mv', ctypes.c_uint8),
    ('seq_force_screen_content_tools', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 5)),
    ('pColorConfig', ctypes.POINTER(StdVideoAV1ColorConfig)),
    ('pTimingInfo', ctypes.POINTER(StdVideoAV1TimingInfo)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoAV1ColorConfig',
        'StdVideoAV1SequenceHeaderFlags',
        'StdVideoAV1TimingInfo',
    },
    'included_in': {
        'VkVideoDecodeAV1SessionParametersCreateInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoAV1SequenceHeaderFlags'},
        'seq_profile': {'python_name': ['seq', 'profile'], 'type': 'StdVideoAV1Profile'},
        'frame_width_bits_minus_1': {'python_name': ['frame', 'width', 'bits', 'minus', '1']},
        'frame_height_bits_minus_1': {'python_name': ['frame', 'height', 'bits', 'minus', '1']},
        'max_frame_width_minus_1': {'python_name': ['max', 'frame', 'width', 'minus', '1']},
        'max_frame_height_minus_1': {'python_name': ['max', 'frame', 'height', 'minus', '1']},
        'delta_frame_id_length_minus_2': {'python_name': ['delta', 'frame', 'id', 'length', 'minus', '2']},
        'additional_frame_id_length_minus_1': {'python_name': ['additional', 'frame', 'id', 'length', 'minus', '1']},
        'order_hint_bits_minus_1': {'python_name': ['order', 'hint', 'bits', 'minus', '1']},
        'seq_force_integer_mv': {'python_name': ['seq', 'force', 'integer', 'mv']},
        'seq_force_screen_content_tools': {'python_name': ['seq', 'force', 'screen', 'content', 'tools']},
        'reserved1': {'python_name': ['reserved1']},
        'pColorConfig': {'python_name': ['p', 'color', 'config'], 'type': 'StdVideoAV1ColorConfig'},
        'pTimingInfo': {'python_name': ['p', 'timing', 'info'], 'type': 'StdVideoAV1TimingInfo'},
    }
}
