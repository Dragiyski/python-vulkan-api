import ctypes

class StdVideoH265ScalingLists(ctypes.Structure):
    _fields_ = [
        ('ScalingList4x4', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6)),
        ('ScalingList8x8', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
        ('ScalingList16x16', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
        ('ScalingList32x32', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 2)),
        ('ScalingListDCCoef16x16', ctypes.ARRAY(ctypes.c_uint8, 6)),
        ('ScalingListDCCoef32x32', ctypes.ARRAY(ctypes.c_uint8, 2)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265PictureParameterSet',
        'StdVideoH265SequenceParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'ScalingList4x4': 'scaling_list4x4',
        'ScalingList8x8': 'scaling_list8x8',
        'ScalingList16x16': 'scaling_list16x16',
        'ScalingList32x32': 'scaling_list32x32',
        'ScalingListDCCoef16x16': 'scaling_list_dccoef16x16',
        'ScalingListDCCoef32x32': 'scaling_list_dccoef32x32',
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

StdVideoH265ScalingLists._type_ = {
    'ScalingList4x4': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6),
    'ScalingList8x8': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6),
    'ScalingList16x16': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6),
    'ScalingList32x32': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 2),
    'ScalingListDCCoef16x16': ctypes.ARRAY(ctypes.c_uint8, 6),
    'ScalingListDCCoef32x32': ctypes.ARRAY(ctypes.c_uint8, 2),
}
