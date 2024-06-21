import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264WeightTableFlags import CType as StdVideoEncodeH264WeightTableFlags

CType._fields_ = [
    ('flags', StdVideoEncodeH264WeightTableFlags),
    ('luma_log2_weight_denom', ctypes.c_uint8),
    ('chroma_log2_weight_denom', ctypes.c_uint8),
    ('luma_weight_l0', ctypes.ARRAY(ctypes.c_int8, 32)),
    ('luma_offset_l0', ctypes.ARRAY(ctypes.c_int8, 32)),
    ('chroma_weight_l0', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32)),
    ('chroma_offset_l0', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32)),
    ('luma_weight_l1', ctypes.ARRAY(ctypes.c_int8, 32)),
    ('luma_offset_l1', ctypes.ARRAY(ctypes.c_int8, 32)),
    ('chroma_weight_l1', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32)),
    ('chroma_offset_l1', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32)),
]
