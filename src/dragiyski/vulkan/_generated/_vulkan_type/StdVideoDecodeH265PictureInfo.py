import ctypes

class StdVideoDecodeH265PictureInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
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
