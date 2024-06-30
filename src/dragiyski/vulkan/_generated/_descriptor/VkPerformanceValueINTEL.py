from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPerformanceValueINTEL'
_member_list_ = ['type', 'data']
_member_info_ = {
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkPerformanceValueTypeINTEL',
        'enum': 'VkPerformanceValueTypeINTEL',
        'is_string': False,
    },
    'data': {
        'type': CComplexType('VkPerformanceValueDataINTEL'),
        'type_name': 'VkPerformanceValueDataINTEL',
        'union': 'VkPerformanceValueDataINTEL',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkPerformanceValueDataINTEL',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPerformanceParameterINTEL',
}
