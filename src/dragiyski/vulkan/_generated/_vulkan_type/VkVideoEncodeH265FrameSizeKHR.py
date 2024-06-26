import ctypes

class VkVideoEncodeH265FrameSizeKHR(ctypes.Structure):
    _fields_ = [
        ('frameISize', ctypes.c_uint32),
        ('framePSize', ctypes.c_uint32),
        ('frameBSize', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkVideoEncodeH265RateControlLayerInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'frameISize': 'frame_isize',
        'framePSize': 'frame_psize',
        'frameBSize': 'frame_bsize',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeH265FrameSizeKHR._type_ = {
    'frameISize': ctypes.c_uint32,
    'framePSize': ctypes.c_uint32,
    'frameBSize': ctypes.c_uint32,
}
