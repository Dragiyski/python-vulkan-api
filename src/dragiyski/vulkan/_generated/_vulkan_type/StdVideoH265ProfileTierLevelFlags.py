import ctypes

class StdVideoH265ProfileTierLevelFlags(ctypes.Structure):
    _fields_ = [
        ('general_tier_flag', ctypes.c_uint32, 1),
        ('general_progressive_source_flag', ctypes.c_uint32, 1),
        ('general_interlaced_source_flag', ctypes.c_uint32, 1),
        ('general_non_packed_constraint_flag', ctypes.c_uint32, 1),
        ('general_frame_only_constraint_flag', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265ProfileTierLevel',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'general_tier_flag': 'general_tier_flag',
        'general_progressive_source_flag': 'general_progressive_source_flag',
        'general_interlaced_source_flag': 'general_interlaced_source_flag',
        'general_non_packed_constraint_flag': 'general_non_packed_constraint_flag',
        'general_frame_only_constraint_flag': 'general_frame_only_constraint_flag',
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

StdVideoH265ProfileTierLevelFlags._type_ = {
    'general_tier_flag': ctypes.c_uint32,
    'general_progressive_source_flag': ctypes.c_uint32,
    'general_interlaced_source_flag': ctypes.c_uint32,
    'general_non_packed_constraint_flag': ctypes.c_uint32,
    'general_frame_only_constraint_flag': ctypes.c_uint32,
}
