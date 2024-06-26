import ctypes

class StdVideoH265HrdParameters(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH265HrdFlags',
        'StdVideoH265SubLayerHrdParameters',
    }
    _included_in_ = {
        'StdVideoH265SequenceParameterSetVui',
        'StdVideoH265VideoParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'tick_divisor_minus2': 'tick_divisor_minus2',
        'du_cpb_removal_delay_increment_length_minus1': 'du_cpb_removal_delay_increment_length_minus1',
        'dpb_output_delay_du_length_minus1': 'dpb_output_delay_du_length_minus1',
        'bit_rate_scale': 'bit_rate_scale',
        'cpb_size_scale': 'cpb_size_scale',
        'cpb_size_du_scale': 'cpb_size_du_scale',
        'initial_cpb_removal_delay_length_minus1': 'initial_cpb_removal_delay_length_minus1',
        'au_cpb_removal_delay_length_minus1': 'au_cpb_removal_delay_length_minus1',
        'dpb_output_delay_length_minus1': 'dpb_output_delay_length_minus1',
        'cpb_cnt_minus1': 'cpb_cnt_minus1',
        'elemental_duration_in_tc_minus1': 'elemental_duration_in_tc_minus1',
        'reserved': 'reserved',
        'pSubLayerHrdParametersNal': 'sub_layer_hrd_parameters_nal',
        'pSubLayerHrdParametersVcl': 'sub_layer_hrd_parameters_vcl',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoH265HrdFlags import StdVideoH265HrdFlags
from .StdVideoH265SubLayerHrdParameters import StdVideoH265SubLayerHrdParameters

StdVideoH265HrdParameters._fields_ = [
    ('flags', StdVideoH265HrdFlags),
    ('tick_divisor_minus2', ctypes.c_uint8),
    ('du_cpb_removal_delay_increment_length_minus1', ctypes.c_uint8),
    ('dpb_output_delay_du_length_minus1', ctypes.c_uint8),
    ('bit_rate_scale', ctypes.c_uint8),
    ('cpb_size_scale', ctypes.c_uint8),
    ('cpb_size_du_scale', ctypes.c_uint8),
    ('initial_cpb_removal_delay_length_minus1', ctypes.c_uint8),
    ('au_cpb_removal_delay_length_minus1', ctypes.c_uint8),
    ('dpb_output_delay_length_minus1', ctypes.c_uint8),
    ('cpb_cnt_minus1', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ('elemental_duration_in_tc_minus1', ctypes.ARRAY(ctypes.c_uint16, 7)),
    ('reserved', ctypes.ARRAY(ctypes.c_uint16, 3)),
    ('pSubLayerHrdParametersNal', ctypes.POINTER(StdVideoH265SubLayerHrdParameters)),
    ('pSubLayerHrdParametersVcl', ctypes.POINTER(StdVideoH265SubLayerHrdParameters)),
]

StdVideoH265HrdParameters._type_ = {
    'flags': StdVideoH265HrdFlags,
    'tick_divisor_minus2': ctypes.c_uint8,
    'du_cpb_removal_delay_increment_length_minus1': ctypes.c_uint8,
    'dpb_output_delay_du_length_minus1': ctypes.c_uint8,
    'bit_rate_scale': ctypes.c_uint8,
    'cpb_size_scale': ctypes.c_uint8,
    'cpb_size_du_scale': ctypes.c_uint8,
    'initial_cpb_removal_delay_length_minus1': ctypes.c_uint8,
    'au_cpb_removal_delay_length_minus1': ctypes.c_uint8,
    'dpb_output_delay_length_minus1': ctypes.c_uint8,
    'cpb_cnt_minus1': ctypes.ARRAY(ctypes.c_uint8, 7),
    'elemental_duration_in_tc_minus1': ctypes.ARRAY(ctypes.c_uint16, 7),
    'reserved': ctypes.ARRAY(ctypes.c_uint16, 3),
    'pSubLayerHrdParametersNal': ctypes.POINTER(StdVideoH265SubLayerHrdParameters),
    'pSubLayerHrdParametersVcl': ctypes.POINTER(StdVideoH265SubLayerHrdParameters),
}
