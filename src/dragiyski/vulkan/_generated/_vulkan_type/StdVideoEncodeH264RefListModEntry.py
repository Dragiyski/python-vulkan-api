import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('modification_of_pic_nums_idc', ctypes.c_int),
        ('abs_diff_pic_num_minus1', ctypes.c_uint16),
        ('long_term_pic_num', ctypes.c_uint16),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH264ReferenceListsInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'modification_of_pic_nums_idc': {'python_name': ['modification', 'of', 'pic', 'nums', 'idc'], 'type': 'StdVideoH264ModificationOfPicNumsIdc'},
        'abs_diff_pic_num_minus1': {'python_name': ['abs', 'diff', 'pic', 'num', 'minus1']},
        'long_term_pic_num': {'python_name': ['long', 'term', 'pic', 'num']},
    }
}
