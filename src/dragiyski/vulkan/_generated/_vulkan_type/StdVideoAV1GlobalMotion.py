import ctypes

class StdVideoAV1GlobalMotion(ctypes.Structure):
    _fields_ = [
        ('GmType', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('gm_params', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int32, 6), 8)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoDecodeAV1PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'GmType': 'gm_type',
        'gm_params': 'gm_params',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoAV1GlobalMotion._type_ = {
    'GmType': ctypes.ARRAY(ctypes.c_uint8, 8),
    'gm_params': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int32, 6), 8),
}
