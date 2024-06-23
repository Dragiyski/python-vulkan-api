import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('ScalingList4x4', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6)),
        ('ScalingList8x8', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
        ('ScalingList16x16', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
        ('ScalingList32x32', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 2)),
        ('ScalingListDCCoef16x16', ctypes.ARRAY(ctypes.c_uint8, 6)),
        ('ScalingListDCCoef32x32', ctypes.ARRAY(ctypes.c_uint8, 2)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265PictureParameterSet',
        'StdVideoH265SequenceParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'ScalingList4x4': {'python_name': ['scaling', 'list4x4']},
        'ScalingList8x8': {'python_name': ['scaling', 'list8x8']},
        'ScalingList16x16': {'python_name': ['scaling', 'list16x16']},
        'ScalingList32x32': {'python_name': ['scaling', 'list32x32']},
        'ScalingListDCCoef16x16': {'python_name': ['scaling', 'list', 'dccoef16x16']},
        'ScalingListDCCoef32x32': {'python_name': ['scaling', 'list', 'dccoef32x32']},
    }
}
