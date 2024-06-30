from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264RefListModEntry'
_member_list_ = ['modification_of_pic_nums_idc', 'abs_diff_pic_num_minus1', 'long_term_pic_num']
_member_info_ = {
    'modification_of_pic_nums_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264ModificationOfPicNumsIdc',
        'enum': 'StdVideoH264ModificationOfPicNumsIdc',
        'is_string': False,
    },
    'abs_diff_pic_num_minus1': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'long_term_pic_num': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoEncodeH264ReferenceListsInfo',
}
_input_of_ = set()
_output_of_ = set()
