import ctypes

class StdVideoEncodeH264ReferenceInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH264ReferenceInfoFlags',
    }
    _included_in_ = {
        'VkVideoEncodeH264DpbSlotInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'primary_pic_type': 'primary_pic_type',
        'FrameNum': 'frame_num',
        'PicOrderCnt': 'pic_order_cnt',
        'long_term_pic_num': 'long_term_pic_num',
        'long_term_frame_idx': 'long_term_frame_idx',
        'temporal_id': 'temporal_id',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std_encode',
    }
    _vk_enum_ = {
        'primary_pic_type': 'StdVideoH264PictureType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoEncodeH264ReferenceInfoFlags import StdVideoEncodeH264ReferenceInfoFlags

StdVideoEncodeH264ReferenceInfo._fields_ = [
    ('flags', StdVideoEncodeH264ReferenceInfoFlags),
    ('primary_pic_type', ctypes.c_int),
    ('FrameNum', ctypes.c_uint32),
    ('PicOrderCnt', ctypes.c_int32),
    ('long_term_pic_num', ctypes.c_uint16),
    ('long_term_frame_idx', ctypes.c_uint16),
    ('temporal_id', ctypes.c_uint8),
]

StdVideoEncodeH264ReferenceInfo._type_ = {
    'flags': StdVideoEncodeH264ReferenceInfoFlags,
    'primary_pic_type': ctypes.c_int,
    'FrameNum': ctypes.c_uint32,
    'PicOrderCnt': ctypes.c_int32,
    'long_term_pic_num': ctypes.c_uint16,
    'long_term_frame_idx': ctypes.c_uint16,
    'temporal_id': ctypes.c_uint8,
}
