from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayProperties2KHR'
_member_list_ = ['sType', 'pNext', 'displayProperties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DISPLAY_PROPERTIES_2_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'displayProperties': {
        'type': CComplexType('VkDisplayPropertiesKHR'),
        'type_name': 'VkDisplayPropertiesKHR',
        'structure': 'VkDisplayPropertiesKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDisplayPropertiesKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceDisplayProperties2KHR',
}
