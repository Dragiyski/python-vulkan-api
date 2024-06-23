import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('scaling_list_present_mask', ctypes.c_uint16),
        ('use_default_scaling_matrix_mask', ctypes.c_uint16),
        ('ScalingList4x4', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6)),
        ('ScalingList8x8', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH264PictureParameterSet',
        'StdVideoH264SequenceParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'scaling_list_present_mask': {'python_name': ['scaling', 'list', 'present', 'mask']},
        'use_default_scaling_matrix_mask': {'python_name': ['use', 'default', 'scaling', 'matrix', 'mask']},
        'ScalingList4x4': {'python_name': ['scaling', 'list4x4']},
        'ScalingList8x8': {'python_name': ['scaling', 'list8x8']},
    }
}
