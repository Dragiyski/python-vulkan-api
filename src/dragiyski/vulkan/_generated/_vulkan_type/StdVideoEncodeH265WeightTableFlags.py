import ctypes

class StdVideoEncodeH265WeightTableFlags(ctypes.Structure):
    _fields_ = [
        ('luma_weight_l0_flag', ctypes.c_uint16),
        ('chroma_weight_l0_flag', ctypes.c_uint16),
        ('luma_weight_l1_flag', ctypes.c_uint16),
        ('chroma_weight_l1_flag', ctypes.c_uint16),
    ]

StdVideoEncodeH265WeightTableFlags._type_ = {
    'luma_weight_l0_flag': ctypes.c_uint16,
    'chroma_weight_l0_flag': ctypes.c_uint16,
    'luma_weight_l1_flag': ctypes.c_uint16,
    'chroma_weight_l1_flag': ctypes.c_uint16,
}
