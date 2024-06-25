import ctypes

class StdVideoEncodeH265ReferenceInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoEncodeH265ReferenceInfoFlags,
            'pic_type': ctypes.c_int,
            'PicOrderCntVal': ctypes.c_int32,
            'TemporalId': ctypes.c_uint8,
        }


from .StdVideoEncodeH265ReferenceInfoFlags import StdVideoEncodeH265ReferenceInfoFlags

StdVideoEncodeH265ReferenceInfo._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceInfoFlags),
    ('pic_type', ctypes.c_int),
    ('PicOrderCntVal', ctypes.c_int32),
    ('TemporalId', ctypes.c_uint8),
]
