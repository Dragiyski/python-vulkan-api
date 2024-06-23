import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('IrapPicFlag', ctypes.c_uint32, 1),
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('IsReference', ctypes.c_uint32, 1),
        ('short_term_ref_pic_set_sps_flag', ctypes.c_uint32, 1),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoDecodeH265PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'IrapPicFlag': {'python_name': ['irap', 'pic', 'flag']},
        'IdrPicFlag': {'python_name': ['idr', 'pic', 'flag']},
        'IsReference': {'python_name': ['is', 'reference']},
        'short_term_ref_pic_set_sps_flag': {'python_name': ['short', 'term', 'ref', 'pic', 'set', 'sps', 'flag']},
    }
}
