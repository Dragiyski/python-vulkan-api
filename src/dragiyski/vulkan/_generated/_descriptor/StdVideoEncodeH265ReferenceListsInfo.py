from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH265ReferenceListsInfo'
_member_list_ = ['flags', 'num_ref_idx_l0_active_minus1', 'num_ref_idx_l1_active_minus1', 'RefPicList0', 'RefPicList1', 'list_entry_l0', 'list_entry_l1']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH265ReferenceListsInfoFlags'),
        'type_name': 'StdVideoEncodeH265ReferenceListsInfoFlags',
        'structure': 'StdVideoEncodeH265ReferenceListsInfoFlags',
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
        'type': CArrayType(CIntType('c_uint8'), 15),
        'is_string': False,
    },
    'RefPicList1': {
        'type': CArrayType(CIntType('c_uint8'), 15),
        'is_string': False,
    },
    'list_entry_l0': {
        'type': CArrayType(CIntType('c_uint8'), 15),
        'is_string': False,
    },
    'list_entry_l1': {
        'type': CArrayType(CIntType('c_uint8'), 15),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH265ReferenceListsInfoFlags',
}
_included_in_ = {
    'StdVideoEncodeH265PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
