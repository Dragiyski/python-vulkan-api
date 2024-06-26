import ctypes

class StdVideoDecodeH265PictureInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoDecodeH265PictureInfoFlags',
    }
    _included_in_ = {
        'VkVideoDecodeH265PictureInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'sps_video_parameter_set_id': 'sps_video_parameter_set_id',
        'pps_seq_parameter_set_id': 'pps_seq_parameter_set_id',
        'pps_pic_parameter_set_id': 'pps_pic_parameter_set_id',
        'NumDeltaPocsOfRefRpsIdx': 'num_delta_pocs_of_ref_rps_idx',
        'PicOrderCntVal': 'pic_order_cnt_val',
        'NumBitsForSTRefPicSetInSlice': 'num_bits_for_stref_pic_set_in_slice',
        'reserved': 'reserved',
        'RefPicSetStCurrBefore': 'ref_pic_set_st_curr_before',
        'RefPicSetStCurrAfter': 'ref_pic_set_st_curr_after',
        'RefPicSetLtCurr': 'ref_pic_set_lt_curr',
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


from .StdVideoDecodeH265PictureInfoFlags import StdVideoDecodeH265PictureInfoFlags

StdVideoDecodeH265PictureInfo._fields_ = [
    ('flags', StdVideoDecodeH265PictureInfoFlags),
    ('sps_video_parameter_set_id', ctypes.c_uint8),
    ('pps_seq_parameter_set_id', ctypes.c_uint8),
    ('pps_pic_parameter_set_id', ctypes.c_uint8),
    ('NumDeltaPocsOfRefRpsIdx', ctypes.c_uint8),
    ('PicOrderCntVal', ctypes.c_int32),
    ('NumBitsForSTRefPicSetInSlice', ctypes.c_uint16),
    ('reserved', ctypes.c_uint16),
    ('RefPicSetStCurrBefore', ctypes.ARRAY(ctypes.c_uint8, 8)),
    ('RefPicSetStCurrAfter', ctypes.ARRAY(ctypes.c_uint8, 8)),
    ('RefPicSetLtCurr', ctypes.ARRAY(ctypes.c_uint8, 8)),
]

StdVideoDecodeH265PictureInfo._type_ = {
    'flags': StdVideoDecodeH265PictureInfoFlags,
    'sps_video_parameter_set_id': ctypes.c_uint8,
    'pps_seq_parameter_set_id': ctypes.c_uint8,
    'pps_pic_parameter_set_id': ctypes.c_uint8,
    'NumDeltaPocsOfRefRpsIdx': ctypes.c_uint8,
    'PicOrderCntVal': ctypes.c_int32,
    'NumBitsForSTRefPicSetInSlice': ctypes.c_uint16,
    'reserved': ctypes.c_uint16,
    'RefPicSetStCurrBefore': ctypes.ARRAY(ctypes.c_uint8, 8),
    'RefPicSetStCurrAfter': ctypes.ARRAY(ctypes.c_uint8, 8),
    'RefPicSetLtCurr': ctypes.ARRAY(ctypes.c_uint8, 8),
}
