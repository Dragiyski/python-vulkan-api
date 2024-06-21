import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('luma_weight_l0_flag', ctypes.c_uint32),
        ('chroma_weight_l0_flag', ctypes.c_uint32),
        ('luma_weight_l1_flag', ctypes.c_uint32),
        ('chroma_weight_l1_flag', ctypes.c_uint32),
    ]