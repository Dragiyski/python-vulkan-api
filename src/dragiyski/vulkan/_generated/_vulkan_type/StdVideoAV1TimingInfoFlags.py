import ctypes

class StdVideoAV1TimingInfoFlags(ctypes.Structure):
    _fields_ = [
        ('equal_picture_interval', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoAV1TimingInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'equal_picture_interval': 'equal_picture_interval',
        'reserved': 'reserved',
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

StdVideoAV1TimingInfoFlags._type_ = {
    'equal_picture_interval': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
