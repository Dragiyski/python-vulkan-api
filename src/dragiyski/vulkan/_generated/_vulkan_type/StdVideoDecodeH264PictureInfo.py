import ctypes

class StdVideoDecodeH264PictureInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoDecodeH264PictureInfoFlags,
            'seq_parameter_set_id': ctypes.c_uint8,
            'pic_parameter_set_id': ctypes.c_uint8,
            'reserved1': ctypes.c_uint8,
            'reserved2': ctypes.c_uint8,
            'frame_num': ctypes.c_uint16,
            'idr_pic_id': ctypes.c_uint16,
            'PicOrderCnt': ctypes.ARRAY(ctypes.c_int32, 2),
        }


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
