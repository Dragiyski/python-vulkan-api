import ctypes

class StdVideoEncodeH265ReferenceInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH265ReferenceInfoFlags',
    }
    _included_in_ = {
        'VkVideoEncodeH265DpbSlotInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'pic_type': 'pic_type',
        'PicOrderCntVal': 'pic_order_cnt_val',
        'TemporalId': 'temporal_id',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std_encode',
    }
    _vk_enum_ = {
        'pic_type': 'StdVideoH265PictureType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoEncodeH265ReferenceInfoFlags import StdVideoEncodeH265ReferenceInfoFlags

StdVideoEncodeH265ReferenceInfo._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceInfoFlags),
    ('pic_type', ctypes.c_int),
    ('PicOrderCntVal', ctypes.c_int32),
    ('TemporalId', ctypes.c_uint8),
]

StdVideoEncodeH265ReferenceInfo._type_ = {
    'flags': StdVideoEncodeH265ReferenceInfoFlags,
    'pic_type': ctypes.c_int,
    'PicOrderCntVal': ctypes.c_int32,
    'TemporalId': ctypes.c_uint8,
}
