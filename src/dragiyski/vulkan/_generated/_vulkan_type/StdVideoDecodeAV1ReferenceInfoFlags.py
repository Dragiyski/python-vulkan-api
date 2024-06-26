import ctypes

class StdVideoDecodeAV1ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('disable_frame_end_update_cdf', ctypes.c_uint32, 1),
        ('segmentation_enabled', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoDecodeAV1ReferenceInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'disable_frame_end_update_cdf': 'disable_frame_end_update_cdf',
        'segmentation_enabled': 'segmentation_enabled',
        'reserved': 'reserved',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std_decode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoDecodeAV1ReferenceInfoFlags._type_ = {
    'disable_frame_end_update_cdf': ctypes.c_uint32,
    'segmentation_enabled': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
