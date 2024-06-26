import ctypes

class StdVideoDecodeH265ReferenceInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoDecodeH265ReferenceInfoFlags',
    }
    _included_in_ = {
        'VkVideoDecodeH265DpbSlotInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'PicOrderCntVal': 'pic_order_cnt_val',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std_decode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoDecodeH265ReferenceInfoFlags import StdVideoDecodeH265ReferenceInfoFlags

StdVideoDecodeH265ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeH265ReferenceInfoFlags),
    ('PicOrderCntVal', ctypes.c_int32),
]

StdVideoDecodeH265ReferenceInfo._type_ = {
    'flags': StdVideoDecodeH265ReferenceInfoFlags,
    'PicOrderCntVal': ctypes.c_int32,
}
