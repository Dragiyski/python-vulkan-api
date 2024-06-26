import ctypes

class StdVideoH265ProfileTierLevel(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH265ProfileTierLevelFlags',
    }
    _included_in_ = {
        'StdVideoH265SequenceParameterSet',
        'StdVideoH265VideoParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'general_profile_idc': 'general_profile_idc',
        'general_level_idc': 'general_level_idc',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std',
    }
    _vk_enum_ = {
        'general_profile_idc': 'StdVideoH265ProfileIdc',
        'general_level_idc': 'StdVideoH265LevelIdc',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoH265ProfileTierLevelFlags import StdVideoH265ProfileTierLevelFlags

StdVideoH265ProfileTierLevel._fields_ = [
    ('flags', StdVideoH265ProfileTierLevelFlags),
    ('general_profile_idc', ctypes.c_int),
    ('general_level_idc', ctypes.c_int),
]

StdVideoH265ProfileTierLevel._type_ = {
    'flags': StdVideoH265ProfileTierLevelFlags,
    'general_profile_idc': ctypes.c_int,
    'general_level_idc': ctypes.c_int,
}
