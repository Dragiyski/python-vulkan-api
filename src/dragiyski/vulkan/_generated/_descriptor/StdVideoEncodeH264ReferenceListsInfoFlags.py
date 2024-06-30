from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264ReferenceListsInfoFlags'
_member_list_ = ['ref_pic_list_modification_flag_l0', 'ref_pic_list_modification_flag_l1', 'reserved']
_member_info_ = {
    'ref_pic_list_modification_flag_l0': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'ref_pic_list_modification_flag_l1': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 30,
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
