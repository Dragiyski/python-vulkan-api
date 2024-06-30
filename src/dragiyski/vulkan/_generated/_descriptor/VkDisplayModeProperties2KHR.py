from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayModeProperties2KHR'
_member_list_ = ['sType', 'pNext', 'displayModeProperties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DISPLAY_MODE_PROPERTIES_2_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'displayModeProperties': {
        'type': CComplexType('VkDisplayModePropertiesKHR'),
        'type_name': 'VkDisplayModePropertiesKHR',
        'structure': 'VkDisplayModePropertiesKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDisplayModePropertiesKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetDisplayModeProperties2KHR',
}
