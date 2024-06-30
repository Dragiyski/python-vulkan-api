from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSpecializationMapEntry'
_member_list_ = ['constantID', 'offset', 'size']
_member_info_ = {
    'constantID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkSpecializationInfo',
}
_input_of_ = set()
_output_of_ = set()
