from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayModeParametersKHR'
_member_list_ = ['visibleRegion', 'refreshRate']
_member_info_ = {
    'visibleRegion': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'refreshRate': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = {
    'VkDisplayModeCreateInfoKHR',
    'VkDisplayModePropertiesKHR',
}
_input_of_ = set()
_output_of_ = set()
