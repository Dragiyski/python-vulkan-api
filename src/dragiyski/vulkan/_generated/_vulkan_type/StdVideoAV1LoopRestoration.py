import ctypes

class StdVideoAV1LoopRestoration(ctypes.Structure):
    _fields_ = [
        ('FrameRestorationType', ctypes.ARRAY(ctypes.c_int, 3)),
        ('LoopRestorationSize', ctypes.ARRAY(ctypes.c_uint16, 3)),
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
        'FrameRestorationType': 'frame_restoration_type',
        'LoopRestorationSize': 'loop_restoration_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std',
    }
    _vk_enum_ = {
        'FrameRestorationType': 'StdVideoAV1FrameRestorationType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoAV1LoopRestoration._type_ = {
    'FrameRestorationType': ctypes.ARRAY(ctypes.c_int, 3),
    'LoopRestorationSize': ctypes.ARRAY(ctypes.c_uint16, 3),
}
