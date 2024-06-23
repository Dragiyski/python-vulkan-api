import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1QuantizationFlags import CType as StdVideoAV1QuantizationFlags

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoAV1QuantizationFlags',
    },
    'included_in': {
        'StdVideoDecodeAV1PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoAV1QuantizationFlags'},
        'base_q_idx': {'python_name': ['base', 'q', 'idx']},
        'DeltaQYDc': {'python_name': ['delta', 'qydc']},
        'DeltaQUDc': {'python_name': ['delta', 'qudc']},
        'DeltaQUAc': {'python_name': ['delta', 'quac']},
        'DeltaQVDc': {'python_name': ['delta', 'qvdc']},
        'DeltaQVAc': {'python_name': ['delta', 'qvac']},
        'qm_y': {'python_name': ['qm', 'y']},
        'qm_u': {'python_name': ['qm', 'u']},
        'qm_v': {'python_name': ['qm', 'v']},
    }
}
