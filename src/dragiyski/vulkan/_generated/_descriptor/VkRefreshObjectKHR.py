from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRefreshObjectKHR'
_member_list_ = ['objectType', 'objectHandle', 'flags']
_member_info_ = {
    'objectType': {
        'type': CIntType('c_int'),
        'type_name': 'VkObjectType',
        'enum': 'VkObjectType',
        'is_string': False,
    },
    'objectHandle': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkRefreshObjectFlagsKHR',
        'enum': 'VkRefreshObjectFlagsKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
