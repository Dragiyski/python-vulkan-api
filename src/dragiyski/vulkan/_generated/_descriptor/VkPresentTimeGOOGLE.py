from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPresentTimeGOOGLE'
_member_list_ = ['presentID', 'desiredPresentTime']
_member_info_ = {
    'presentID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'desiredPresentTime': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPresentTimesInfoGOOGLE',
}
_input_of_ = set()
_output_of_ = set()
