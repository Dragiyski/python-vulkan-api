import ctypes, sys

class StdVideoH264PictureParameterSet(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoH264PictureParameterSet

from . import StdVideoH264ScalingLists
from . import StdVideoH264PpsFlags

StdVideoH264PictureParameterSet._fields_ = [
    ('flags', StdVideoH264PpsFlags),
    ('seq_parameter_set_id', ctypes.c_uint8),
    ('pic_parameter_set_id', ctypes.c_uint8),
    ('num_ref_idx_l0_default_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_default_active_minus1', ctypes.c_uint8),
    ('weighted_bipred_idc', ctypes.c_int),
    ('pic_init_qp_minus26', ctypes.c_int8),
    ('pic_init_qs_minus26', ctypes.c_int8),
    ('chroma_qp_index_offset', ctypes.c_int8),
    ('second_chroma_qp_index_offset', ctypes.c_int8),
    ('pScalingLists', ctypes.POINTER(StdVideoH264ScalingLists)),
]
