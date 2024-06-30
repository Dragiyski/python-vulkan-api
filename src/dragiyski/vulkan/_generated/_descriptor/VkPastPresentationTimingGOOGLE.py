from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPastPresentationTimingGOOGLE'
_member_list_ = ['presentID', 'desiredPresentTime', 'actualPresentTime', 'earliestPresentTime', 'presentMargin']
_member_info_ = {
    'presentID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'desiredPresentTime': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'actualPresentTime': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'earliestPresentTime': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'presentMargin': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPastPresentationTimingGOOGLE',
}
