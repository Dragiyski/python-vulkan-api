import ctypes

class StdVideoH264ScalingLists(ctypes.Structure):
    _fields_ = [
        ('scaling_list_present_mask', ctypes.c_uint16),
        ('use_default_scaling_matrix_mask', ctypes.c_uint16),
        ('ScalingList4x4', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6)),
        ('ScalingList8x8', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH264PictureParameterSet',
        'StdVideoH264SequenceParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'scaling_list_present_mask': 'scaling_list_present_mask',
        'use_default_scaling_matrix_mask': 'use_default_scaling_matrix_mask',
        'ScalingList4x4': 'scaling_list4x4',
        'ScalingList8x8': 'scaling_list8x8',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoH264ScalingLists._type_ = {
    'scaling_list_present_mask': ctypes.c_uint16,
    'use_default_scaling_matrix_mask': ctypes.c_uint16,
    'ScalingList4x4': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6),
    'ScalingList8x8': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6),
}
