import ctypes

class StdVideoDecodeH264PictureInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoDecodeH264PictureInfoFlags',
    }
    _included_in_ = {
        'VkVideoDecodeH264PictureInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'seq_parameter_set_id': 'seq_parameter_set_id',
        'pic_parameter_set_id': 'pic_parameter_set_id',
        'reserved1': 'reserved1',
        'reserved2': 'reserved2',
        'frame_num': 'frame_num',
        'idr_pic_id': 'idr_pic_id',
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


from .StdVideoDecodeH264PictureInfoFlags import StdVideoDecodeH264PictureInfoFlags

StdVideoDecodeH264PictureInfo._fields_ = [
    ('flags', StdVideoDecodeH264PictureInfoFlags),
    ('seq_parameter_set_id', ctypes.c_uint8),
    ('pic_parameter_set_id', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('reserved2', ctypes.c_uint8),
    ('frame_num', ctypes.c_uint16),
    ('idr_pic_id', ctypes.c_uint16),
    ('PicOrderCnt', ctypes.ARRAY(ctypes.c_int32, 2)),
]

StdVideoDecodeH264PictureInfo._type_ = {
    'flags': StdVideoDecodeH264PictureInfoFlags,
    'seq_parameter_set_id': ctypes.c_uint8,
    'pic_parameter_set_id': ctypes.c_uint8,
    'reserved1': ctypes.c_uint8,
    'reserved2': ctypes.c_uint8,
    'frame_num': ctypes.c_uint16,
    'idr_pic_id': ctypes.c_uint16,
    'PicOrderCnt': ctypes.ARRAY(ctypes.c_int32, 2),
}
