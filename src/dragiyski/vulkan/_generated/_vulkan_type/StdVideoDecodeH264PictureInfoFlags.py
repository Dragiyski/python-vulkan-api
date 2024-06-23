import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('field_pic_flag', ctypes.c_uint32, 1),
        ('is_intra', ctypes.c_uint32, 1),
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('bottom_field_flag', ctypes.c_uint32, 1),
        ('is_reference', ctypes.c_uint32, 1),
        ('complementary_field_pair', ctypes.c_uint32, 1),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoDecodeH264PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'field_pic_flag': {'python_name': ['field', 'pic', 'flag']},
        'is_intra': {'python_name': ['is', 'intra']},
        'IdrPicFlag': {'python_name': ['idr', 'pic', 'flag']},
        'bottom_field_flag': {'python_name': ['bottom', 'field', 'flag']},
        'is_reference': {'python_name': ['is', 'reference']},
        'complementary_field_pair': {'python_name': ['complementary', 'field', 'pair']},
    }
}
