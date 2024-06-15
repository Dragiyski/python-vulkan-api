import ctypes, sys

class StdVideoEncodeH265WeightTableFlags(ctypes.Structure):
    _fields_ = [
        ('luma_weight_l0_flag', ctypes.c_uint16),
        ('chroma_weight_l0_flag', ctypes.c_uint16),
        ('luma_weight_l1_flag', ctypes.c_uint16),
        ('chroma_weight_l1_flag', ctypes.c_uint16),
    ]

sys.modules[__name__] = StdVideoEncodeH265WeightTableFlags
