import ctypes

class StdVideoEncodeH265PictureInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH265LongTermRefPics',
        'StdVideoEncodeH265PictureInfoFlags',
        'StdVideoEncodeH265ReferenceListsInfo',
        'StdVideoH265ShortTermRefPicSet',
    }
    _included_in_ = {
        'VkVideoEncodeH265PictureInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'pic_type': 'pic_type',
        'sps_video_parameter_set_id': 'sps_video_parameter_set_id',
        'pps_seq_parameter_set_id': 'pps_seq_parameter_set_id',
        'pps_pic_parameter_set_id': 'pps_pic_parameter_set_id',
        'short_term_ref_pic_set_idx': 'short_term_ref_pic_set_idx',
        'PicOrderCntVal': 'pic_order_cnt_val',
        'TemporalId': 'temporal_id',
        'reserved1': 'reserved1',
        'pRefLists': 'ref_lists',
        'pShortTermRefPicSet': 'short_term_ref_pic_set',
        'pLongTermRefPics': 'long_term_ref_pics',
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


from .StdVideoEncodeH265LongTermRefPics import StdVideoEncodeH265LongTermRefPics
from .StdVideoEncodeH265PictureInfoFlags import StdVideoEncodeH265PictureInfoFlags
from .StdVideoEncodeH265ReferenceListsInfo import StdVideoEncodeH265ReferenceListsInfo
from .StdVideoH265ShortTermRefPicSet import StdVideoH265ShortTermRefPicSet

StdVideoEncodeH265PictureInfo._fields_ = [
    ('flags', StdVideoEncodeH265PictureInfoFlags),
    ('pic_type', ctypes.c_int),
    ('sps_video_parameter_set_id', ctypes.c_uint8),
    ('pps_seq_parameter_set_id', ctypes.c_uint8),
    ('pps_pic_parameter_set_id', ctypes.c_uint8),
    ('short_term_ref_pic_set_idx', ctypes.c_uint8),
    ('PicOrderCntVal', ctypes.c_int32),
    ('TemporalId', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ('pRefLists', ctypes.POINTER(StdVideoEncodeH265ReferenceListsInfo)),
    ('pShortTermRefPicSet', ctypes.POINTER(StdVideoH265ShortTermRefPicSet)),
    ('pLongTermRefPics', ctypes.POINTER(StdVideoEncodeH265LongTermRefPics)),
]

StdVideoEncodeH265PictureInfo._type_ = {
    'flags': StdVideoEncodeH265PictureInfoFlags,
    'pic_type': ctypes.c_int,
    'sps_video_parameter_set_id': ctypes.c_uint8,
    'pps_seq_parameter_set_id': ctypes.c_uint8,
    'pps_pic_parameter_set_id': ctypes.c_uint8,
    'short_term_ref_pic_set_idx': ctypes.c_uint8,
    'PicOrderCntVal': ctypes.c_int32,
    'TemporalId': ctypes.c_uint8,
    'reserved1': ctypes.ARRAY(ctypes.c_uint8, 7),
    'pRefLists': ctypes.POINTER(StdVideoEncodeH265ReferenceListsInfo),
    'pShortTermRefPicSet': ctypes.POINTER(StdVideoH265ShortTermRefPicSet),
    'pLongTermRefPics': ctypes.POINTER(StdVideoEncodeH265LongTermRefPics),
}
