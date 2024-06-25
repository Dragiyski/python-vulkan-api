import ctypes

class StdVideoDecodeH265ReferenceInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoDecodeH265ReferenceInfoFlags,
            'PicOrderCntVal': ctypes.c_int32,
        }


from .StdVideoDecodeH265ReferenceInfoFlags import StdVideoDecodeH265ReferenceInfoFlags

StdVideoDecodeH265ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeH265ReferenceInfoFlags),
    ('PicOrderCntVal', ctypes.c_int32),
]
