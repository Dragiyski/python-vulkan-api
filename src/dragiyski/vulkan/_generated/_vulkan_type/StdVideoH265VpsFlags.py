import ctypes

class StdVideoH265VpsFlags(ctypes.Structure):
    _fields_ = [
        ('vps_temporal_id_nesting_flag', ctypes.c_uint32, 1),
        ('vps_sub_layer_ordering_info_present_flag', ctypes.c_uint32, 1),
        ('vps_timing_info_present_flag', ctypes.c_uint32, 1),
        ('vps_poc_proportional_to_timing_flag', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265VideoParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'vps_temporal_id_nesting_flag': 'vps_temporal_id_nesting_flag',
        'vps_sub_layer_ordering_info_present_flag': 'vps_sub_layer_ordering_info_present_flag',
        'vps_timing_info_present_flag': 'vps_timing_info_present_flag',
        'vps_poc_proportional_to_timing_flag': 'vps_poc_proportional_to_timing_flag',
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

StdVideoH265VpsFlags._type_ = {
    'vps_temporal_id_nesting_flag': ctypes.c_uint32,
    'vps_sub_layer_ordering_info_present_flag': ctypes.c_uint32,
    'vps_timing_info_present_flag': ctypes.c_uint32,
    'vps_poc_proportional_to_timing_flag': ctypes.c_uint32,
}
