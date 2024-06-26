import ctypes

class StdVideoEncodeH264PictureInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH264PictureInfoFlags',
        'StdVideoEncodeH264ReferenceListsInfo',
    }
    _included_in_ = {
        'VkVideoEncodeH264PictureInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'seq_parameter_set_id': 'seq_parameter_set_id',
        'pic_parameter_set_id': 'pic_parameter_set_id',
        'idr_pic_id': 'idr_pic_id',
        'primary_pic_type': 'primary_pic_type',
        'frame_num': 'frame_num',
        'PicOrderCnt': 'pic_order_cnt',
        'temporal_id': 'temporal_id',
        'reserved1': 'reserved1',
        'pRefLists': 'ref_lists',
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


from .StdVideoEncodeH264PictureInfoFlags import StdVideoEncodeH264PictureInfoFlags
from .StdVideoEncodeH264ReferenceListsInfo import StdVideoEncodeH264ReferenceListsInfo

StdVideoEncodeH264PictureInfo._fields_ = [
    ('flags', StdVideoEncodeH264PictureInfoFlags),
    ('seq_parameter_set_id', ctypes.c_uint8),
    ('pic_parameter_set_id', ctypes.c_uint8),
    ('idr_pic_id', ctypes.c_uint16),
    ('primary_pic_type', ctypes.c_int),
    ('frame_num', ctypes.c_uint32),
    ('PicOrderCnt', ctypes.c_int32),
    ('temporal_id', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 3)),
    ('pRefLists', ctypes.POINTER(StdVideoEncodeH264ReferenceListsInfo)),
]

StdVideoEncodeH264PictureInfo._type_ = {
    'flags': StdVideoEncodeH264PictureInfoFlags,
    'seq_parameter_set_id': ctypes.c_uint8,
    'pic_parameter_set_id': ctypes.c_uint8,
    'idr_pic_id': ctypes.c_uint16,
    'primary_pic_type': ctypes.c_int,
    'frame_num': ctypes.c_uint32,
    'PicOrderCnt': ctypes.c_int32,
    'temporal_id': ctypes.c_uint8,
    'reserved1': ctypes.ARRAY(ctypes.c_uint8, 3),
    'pRefLists': ctypes.POINTER(StdVideoEncodeH264ReferenceListsInfo),
}
