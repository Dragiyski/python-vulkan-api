from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayModePropertiesKHR'
_member_list_ = ['displayMode', 'parameters']
_member_info_ = {
    'displayMode': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'parameters': {
        'type': CComplexType('VkDisplayModeParametersKHR'),
        'type_name': 'VkDisplayModeParametersKHR',
        'structure': 'VkDisplayModeParametersKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDisplayModeParametersKHR',
}
_included_in_ = {
    'VkDisplayModeProperties2KHR',
}
_input_of_ = set()
_output_of_ = {
    'vkGetDisplayModePropertiesKHR',
}
