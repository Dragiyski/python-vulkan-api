import ctypes

class StdVideoEncodeH265WeightTable(ctypes.Structure):
    pass

from .StdVideoEncodeH265WeightTableFlags import StdVideoEncodeH265WeightTableFlags

StdVideoEncodeH265WeightTable._fields_ = [
    ('flags', StdVideoEncodeH265WeightTableFlags),
    ('luma_log2_weight_denom', ctypes.c_uint8),
    ('delta_chroma_log2_weight_denom', ctypes.c_int8),
    ('delta_luma_weight_l0', ctypes.ARRAY(ctypes.c_int8, 15)),
    ('luma_offset_l0', ctypes.ARRAY(ctypes.c_int8, 15)),
    ('delta_chroma_weight_l0', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15)),
    ('delta_chroma_offset_l0', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15)),
    ('delta_luma_weight_l1', ctypes.ARRAY(ctypes.c_int8, 15)),
    ('luma_offset_l1', ctypes.ARRAY(ctypes.c_int8, 15)),
    ('delta_chroma_weight_l1', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15)),
    ('delta_chroma_offset_l1', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15)),
]

StdVideoEncodeH265WeightTable._type_ = {
    'flags': StdVideoEncodeH265WeightTableFlags,
    'luma_log2_weight_denom': ctypes.c_uint8,
    'delta_chroma_log2_weight_denom': ctypes.c_int8,
    'delta_luma_weight_l0': ctypes.ARRAY(ctypes.c_int8, 15),
    'luma_offset_l0': ctypes.ARRAY(ctypes.c_int8, 15),
    'delta_chroma_weight_l0': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15),
    'delta_chroma_offset_l0': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15),
    'delta_luma_weight_l1': ctypes.ARRAY(ctypes.c_int8, 15),
    'luma_offset_l1': ctypes.ARRAY(ctypes.c_int8, 15),
    'delta_chroma_weight_l1': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15),
    'delta_chroma_offset_l1': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15),
}
