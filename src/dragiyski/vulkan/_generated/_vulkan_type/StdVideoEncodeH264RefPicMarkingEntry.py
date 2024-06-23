import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('memory_management_control_operation', ctypes.c_int),
        ('difference_of_pic_nums_minus1', ctypes.c_uint16),
        ('long_term_pic_num', ctypes.c_uint16),
        ('long_term_frame_idx', ctypes.c_uint16),
        ('max_long_term_frame_idx_plus1', ctypes.c_uint16),
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
        'memory_management_control_operation': {'python_name': ['memory', 'management', 'control', 'operation'], 'type': 'StdVideoH264MemMgmtControlOp'},
        'difference_of_pic_nums_minus1': {'python_name': ['difference', 'of', 'pic', 'nums', 'minus1']},
        'long_term_pic_num': {'python_name': ['long', 'term', 'pic', 'num']},
        'long_term_frame_idx': {'python_name': ['long', 'term', 'frame', 'idx']},
        'max_long_term_frame_idx_plus1': {'python_name': ['max', 'long', 'term', 'frame', 'idx', 'plus1']},
    }
}
