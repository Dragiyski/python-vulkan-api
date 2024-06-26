import ctypes

class StdVideoH264SequenceParameterSetVui(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH264HrdParameters',
        'StdVideoH264SpsVuiFlags',
    }
    _included_in_ = {
        'StdVideoH264SequenceParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'aspect_ratio_idc': 'aspect_ratio_idc',
        'sar_width': 'sar_width',
        'sar_height': 'sar_height',
        'video_format': 'video_format',
        'colour_primaries': 'colour_primaries',
        'transfer_characteristics': 'transfer_characteristics',
        'matrix_coefficients': 'matrix_coefficients',
        'num_units_in_tick': 'num_units_in_tick',
        'time_scale': 'time_scale',
        'max_num_reorder_frames': 'max_num_reorder_frames',
        'max_dec_frame_buffering': 'max_dec_frame_buffering',
        'chroma_sample_loc_type_top_field': 'chroma_sample_loc_type_top_field',
        'chroma_sample_loc_type_bottom_field': 'chroma_sample_loc_type_bottom_field',
        'reserved1': 'reserved1',
        'pHrdParameters': 'hrd_parameters',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std',
    }
    _vk_enum_ = {
        'aspect_ratio_idc': 'StdVideoH264AspectRatioIdc',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoH264HrdParameters import StdVideoH264HrdParameters
from .StdVideoH264SpsVuiFlags import StdVideoH264SpsVuiFlags

StdVideoH264SequenceParameterSetVui._fields_ = [
    ('flags', StdVideoH264SpsVuiFlags),
    ('aspect_ratio_idc', ctypes.c_int),
    ('sar_width', ctypes.c_uint16),
    ('sar_height', ctypes.c_uint16),
    ('video_format', ctypes.c_uint8),
    ('colour_primaries', ctypes.c_uint8),
    ('transfer_characteristics', ctypes.c_uint8),
    ('matrix_coefficients', ctypes.c_uint8),
    ('num_units_in_tick', ctypes.c_uint32),
    ('time_scale', ctypes.c_uint32),
    ('max_num_reorder_frames', ctypes.c_uint8),
    ('max_dec_frame_buffering', ctypes.c_uint8),
    ('chroma_sample_loc_type_top_field', ctypes.c_uint8),
    ('chroma_sample_loc_type_bottom_field', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint32),
    ('pHrdParameters', ctypes.POINTER(StdVideoH264HrdParameters)),
]

StdVideoH264SequenceParameterSetVui._type_ = {
    'flags': StdVideoH264SpsVuiFlags,
    'aspect_ratio_idc': ctypes.c_int,
    'sar_width': ctypes.c_uint16,
    'sar_height': ctypes.c_uint16,
    'video_format': ctypes.c_uint8,
    'colour_primaries': ctypes.c_uint8,
    'transfer_characteristics': ctypes.c_uint8,
    'matrix_coefficients': ctypes.c_uint8,
    'num_units_in_tick': ctypes.c_uint32,
    'time_scale': ctypes.c_uint32,
    'max_num_reorder_frames': ctypes.c_uint8,
    'max_dec_frame_buffering': ctypes.c_uint8,
    'chroma_sample_loc_type_top_field': ctypes.c_uint8,
    'chroma_sample_loc_type_bottom_field': ctypes.c_uint8,
    'reserved1': ctypes.c_uint32,
    'pHrdParameters': ctypes.POINTER(StdVideoH264HrdParameters),
}
