import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264RefListModEntry import CType as StdVideoEncodeH264RefListModEntry
from .StdVideoEncodeH264RefPicMarkingEntry import CType as StdVideoEncodeH264RefPicMarkingEntry
from .StdVideoEncodeH264ReferenceListsInfoFlags import CType as StdVideoEncodeH264ReferenceListsInfoFlags

CType._fields_ = [
    ('flags', StdVideoEncodeH264ReferenceListsInfoFlags),
    ('num_ref_idx_l0_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_active_minus1', ctypes.c_uint8),
    ('RefPicList0', ctypes.ARRAY(ctypes.c_uint8, 32)),
    ('RefPicList1', ctypes.ARRAY(ctypes.c_uint8, 32)),
    ('refList0ModOpCount', ctypes.c_uint8),
    ('refList1ModOpCount', ctypes.c_uint8),
    ('refPicMarkingOpCount', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ('pRefList0ModOperations', ctypes.POINTER(StdVideoEncodeH264RefListModEntry)),
    ('pRefList1ModOperations', ctypes.POINTER(StdVideoEncodeH264RefListModEntry)),
    ('pRefPicMarkingOperations', ctypes.POINTER(StdVideoEncodeH264RefPicMarkingEntry)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH264RefListModEntry',
        'StdVideoEncodeH264RefPicMarkingEntry',
        'StdVideoEncodeH264ReferenceListsInfoFlags',
    },
    'included_in': {
        'StdVideoEncodeH264PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH264ReferenceListsInfoFlags'},
        'num_ref_idx_l0_active_minus1': {'python_name': ['num', 'ref', 'idx', 'l0', 'active', 'minus1']},
        'num_ref_idx_l1_active_minus1': {'python_name': ['num', 'ref', 'idx', 'l1', 'active', 'minus1']},
        'RefPicList0': {'python_name': ['ref', 'pic', 'list0']},
        'RefPicList1': {'python_name': ['ref', 'pic', 'list1']},
        'refList0ModOpCount': {'python_name': ['ref', 'list0', 'mod', 'op', 'count']},
        'refList1ModOpCount': {'python_name': ['ref', 'list1', 'mod', 'op', 'count']},
        'refPicMarkingOpCount': {'python_name': ['ref', 'pic', 'marking', 'op', 'count']},
        'reserved1': {'python_name': ['reserved1']},
        'pRefList0ModOperations': {'python_name': ['p', 'ref', 'list0', 'mod', 'operations'], 'type': 'StdVideoEncodeH264RefListModEntry'},
        'pRefList1ModOperations': {'python_name': ['p', 'ref', 'list1', 'mod', 'operations'], 'type': 'StdVideoEncodeH264RefListModEntry'},
        'pRefPicMarkingOperations': {'python_name': ['p', 'ref', 'pic', 'marking', 'operations'], 'type': 'StdVideoEncodeH264RefPicMarkingEntry'},
    }
}
