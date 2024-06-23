import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('FeatureEnabled', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('FeatureData', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int16, 8), 8)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoDecodeAV1PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'FeatureEnabled': {'python_name': ['feature', 'enabled']},
        'FeatureData': {'python_name': ['feature', 'data']},
    }
}
