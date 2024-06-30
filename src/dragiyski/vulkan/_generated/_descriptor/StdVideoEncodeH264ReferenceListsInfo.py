from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264ReferenceListsInfo'
_member_list_ = ['flags', 'num_ref_idx_l0_active_minus1', 'num_ref_idx_l1_active_minus1', 'RefPicList0', 'RefPicList1', 'refList0ModOpCount', 'refList1ModOpCount', 'refPicMarkingOpCount', 'reserved1', 'pRefList0ModOperations', 'pRefList1ModOperations', 'pRefPicMarkingOperations']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH264ReferenceListsInfoFlags'),
        'type_name': 'StdVideoEncodeH264ReferenceListsInfoFlags',
        'structure': 'StdVideoEncodeH264ReferenceListsInfoFlags',
        'is_string': False,
    },
    'num_ref_idx_l0_active_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_ref_idx_l1_active_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'RefPicList0': {
        'type': CArrayType(CIntType('c_uint8'), 32),
        'is_string': False,
    },
    'RefPicList1': {
        'type': CArrayType(CIntType('c_uint8'), 32),
        'is_string': False,
    },
    'refList0ModOpCount': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'refList1ModOpCount': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'refPicMarkingOpCount': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CArrayType(CIntType('c_uint8'), 7),
        'is_string': False,
    },
    'pRefList0ModOperations': {
        'type': CPointerType(CComplexType('StdVideoEncodeH264RefListModEntry')),
        'type_name': 'StdVideoEncodeH264RefListModEntry',
        'structure': 'StdVideoEncodeH264RefListModEntry',
        'is_string': False,
    },
    'pRefList1ModOperations': {
        'type': CPointerType(CComplexType('StdVideoEncodeH264RefListModEntry')),
        'type_name': 'StdVideoEncodeH264RefListModEntry',
        'structure': 'StdVideoEncodeH264RefListModEntry',
        'is_string': False,
    },
    'pRefPicMarkingOperations': {
        'type': CPointerType(CComplexType('StdVideoEncodeH264RefPicMarkingEntry')),
        'type_name': 'StdVideoEncodeH264RefPicMarkingEntry',
        'structure': 'StdVideoEncodeH264RefPicMarkingEntry',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH264RefListModEntry',
    'StdVideoEncodeH264RefPicMarkingEntry',
    'StdVideoEncodeH264ReferenceListsInfoFlags',
}
_included_in_ = {
    'StdVideoEncodeH264PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
