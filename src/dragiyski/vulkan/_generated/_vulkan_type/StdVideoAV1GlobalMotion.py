import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('GmType', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('gm_params', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int32, 6), 8)),
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
        'GmType': {'python_name': ['gm', 'type']},
        'gm_params': {'python_name': ['gm', 'params']},
    }
}
