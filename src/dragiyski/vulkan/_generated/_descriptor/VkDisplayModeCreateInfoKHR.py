from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayModeCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'parameters']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DISPLAY_MODE_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDisplayModeCreateFlagsKHR',
        'enum': 'VkDisplayModeCreateFlagsKHR',
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
_included_in_ = set()
_input_of_ = {
    'vkCreateDisplayModeKHR',
}
_output_of_ = set()
