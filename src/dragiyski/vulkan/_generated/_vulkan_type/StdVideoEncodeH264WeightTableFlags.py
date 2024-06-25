import ctypes

class StdVideoEncodeH264WeightTableFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'luma_weight_l0_flag': ctypes.c_uint32,
            'chroma_weight_l0_flag': ctypes.c_uint32,
            'luma_weight_l1_flag': ctypes.c_uint32,
            'chroma_weight_l1_flag': ctypes.c_uint32,
        }

    _fields_ = [
        ('luma_weight_l0_flag', ctypes.c_uint32),
        ('chroma_weight_l0_flag', ctypes.c_uint32),
        ('luma_weight_l1_flag', ctypes.c_uint32),
        ('chroma_weight_l1_flag', ctypes.c_uint32),
    ]
