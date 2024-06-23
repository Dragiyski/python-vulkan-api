import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('ref_pic_list_modification_flag_l0', ctypes.c_uint32, 1),
        ('ref_pic_list_modification_flag_l1', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH265ReferenceListsInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'ref_pic_list_modification_flag_l0': {'python_name': ['ref', 'pic', 'list', 'modification', 'flag', 'l0']},
        'ref_pic_list_modification_flag_l1': {'python_name': ['ref', 'pic', 'list', 'modification', 'flag', 'l1']},
        'reserved': {'python_name': ['reserved']},
    }
}
