from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264RefPicMarkingEntry'
_member_list_ = ['memory_management_control_operation', 'difference_of_pic_nums_minus1', 'long_term_pic_num', 'long_term_frame_idx', 'max_long_term_frame_idx_plus1']
_member_info_ = {
    'memory_management_control_operation': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264MemMgmtControlOp',
        'enum': 'StdVideoH264MemMgmtControlOp',
        'is_string': False,
    },
    'difference_of_pic_nums_minus1': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'long_term_pic_num': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'long_term_frame_idx': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'max_long_term_frame_idx_plus1': {
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
