import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265ReferenceListsInfoFlags import CType as StdVideoEncodeH265ReferenceListsInfoFlags

CType._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceListsInfoFlags),
    ('num_ref_idx_l0_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_active_minus1', ctypes.c_uint8),
    ('RefPicList0', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('RefPicList1', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('list_entry_l0', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('list_entry_l1', ctypes.ARRAY(ctypes.c_uint8, 15)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH265ReferenceListsInfoFlags',
    },
    'included_in': {
        'StdVideoEncodeH265PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH265ReferenceListsInfoFlags'},
        'num_ref_idx_l0_active_minus1': {'python_name': ['num', 'ref', 'idx', 'l0', 'active', 'minus1']},
        'num_ref_idx_l1_active_minus1': {'python_name': ['num', 'ref', 'idx', 'l1', 'active', 'minus1']},
        'RefPicList0': {'python_name': ['ref', 'pic', 'list0']},
        'RefPicList1': {'python_name': ['ref', 'pic', 'list1']},
        'list_entry_l0': {'python_name': ['list', 'entry', 'l0']},
        'list_entry_l1': {'python_name': ['list', 'entry', 'l1']},
    }
}
