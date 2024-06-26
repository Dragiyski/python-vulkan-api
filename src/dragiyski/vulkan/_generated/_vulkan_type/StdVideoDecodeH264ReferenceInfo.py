import ctypes

class StdVideoDecodeH264ReferenceInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoDecodeH264ReferenceInfoFlags',
    }
    _included_in_ = {
        'VkVideoDecodeH264DpbSlotInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'FrameNum': 'frame_num',
        'reserved': 'reserved',
        'PicOrderCnt': 'pic_order_cnt',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std_decode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoDecodeH264ReferenceInfoFlags import StdVideoDecodeH264ReferenceInfoFlags

StdVideoDecodeH264ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeH264ReferenceInfoFlags),
    ('FrameNum', ctypes.c_uint16),
    ('reserved', ctypes.c_uint16),
    ('PicOrderCnt', ctypes.ARRAY(ctypes.c_int32, 2)),
]

StdVideoDecodeH264ReferenceInfo._type_ = {
    'flags': StdVideoDecodeH264ReferenceInfoFlags,
    'FrameNum': ctypes.c_uint16,
    'reserved': ctypes.c_uint16,
    'PicOrderCnt': ctypes.ARRAY(ctypes.c_int32, 2),
}
