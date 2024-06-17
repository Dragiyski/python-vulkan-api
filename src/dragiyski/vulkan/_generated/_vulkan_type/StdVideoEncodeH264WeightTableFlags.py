import ctypes, sys

class StdVideoEncodeH264WeightTableFlags(ctypes.Structure):
    _fields_ = [
        ('luma_weight_l0_flag', ctypes.c_uint32),
        ('chroma_weight_l0_flag', ctypes.c_uint32),
        ('luma_weight_l1_flag', ctypes.c_uint32),
        ('chroma_weight_l1_flag', ctypes.c_uint32),
    ]

sys.modules[__name__] = StdVideoEncodeH264WeightTableFlags
