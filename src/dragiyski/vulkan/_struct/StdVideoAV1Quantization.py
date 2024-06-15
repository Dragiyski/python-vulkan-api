import ctypes, sys

class StdVideoAV1Quantization(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoAV1Quantization

from . import StdVideoAV1QuantizationFlags

StdVideoAV1Quantization._fields_ = [
    ('flags', StdVideoAV1QuantizationFlags),
    ('base_q_idx', ctypes.c_uint8),
    ('DeltaQYDc', ctypes.c_int8),
    ('DeltaQUDc', ctypes.c_int8),
    ('DeltaQUAc', ctypes.c_int8),
    ('DeltaQVDc', ctypes.c_int8),
    ('DeltaQVAc', ctypes.c_int8),
    ('qm_y', ctypes.c_uint8),
    ('qm_u', ctypes.c_uint8),
    ('qm_v', ctypes.c_uint8),
]
