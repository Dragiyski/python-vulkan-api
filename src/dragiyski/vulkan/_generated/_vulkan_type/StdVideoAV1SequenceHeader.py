import ctypes

class StdVideoAV1SequenceHeader(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoAV1ColorConfig',
        'StdVideoAV1SequenceHeaderFlags',
        'StdVideoAV1TimingInfo',
    }
    _included_in_ = {
        'VkVideoDecodeAV1SessionParametersCreateInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'seq_profile': 'seq_profile',
        'frame_width_bits_minus_1': 'frame_width_bits_minus_1',
        'frame_height_bits_minus_1': 'frame_height_bits_minus_1',
        'max_frame_width_minus_1': 'max_frame_width_minus_1',
        'max_frame_height_minus_1': 'max_frame_height_minus_1',
        'delta_frame_id_length_minus_2': 'delta_frame_id_length_minus_2',
        'additional_frame_id_length_minus_1': 'additional_frame_id_length_minus_1',
        'order_hint_bits_minus_1': 'order_hint_bits_minus_1',
        'seq_force_integer_mv': 'seq_force_integer_mv',
        'seq_force_screen_content_tools': 'seq_force_screen_content_tools',
        'reserved1': 'reserved1',
        'pColorConfig': 'color_config',
        'pTimingInfo': 'timing_info',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std',
    }
    _vk_enum_ = {
        'seq_profile': 'StdVideoAV1Profile',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoAV1ColorConfig import StdVideoAV1ColorConfig
from .StdVideoAV1SequenceHeaderFlags import StdVideoAV1SequenceHeaderFlags
from .StdVideoAV1TimingInfo import StdVideoAV1TimingInfo

StdVideoAV1SequenceHeader._fields_ = [
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

StdVideoAV1SequenceHeader._type_ = {
    'flags': StdVideoAV1SequenceHeaderFlags,
    'seq_profile': ctypes.c_int,
    'frame_width_bits_minus_1': ctypes.c_uint8,
    'frame_height_bits_minus_1': ctypes.c_uint8,
    'max_frame_width_minus_1': ctypes.c_uint16,
    'max_frame_height_minus_1': ctypes.c_uint16,
    'delta_frame_id_length_minus_2': ctypes.c_uint8,
    'additional_frame_id_length_minus_1': ctypes.c_uint8,
    'order_hint_bits_minus_1': ctypes.c_uint8,
    'seq_force_integer_mv': ctypes.c_uint8,
    'seq_force_screen_content_tools': ctypes.c_uint8,
    'reserved1': ctypes.ARRAY(ctypes.c_uint8, 5),
    'pColorConfig': ctypes.POINTER(StdVideoAV1ColorConfig),
    'pTimingInfo': ctypes.POINTER(StdVideoAV1TimingInfo),
}
