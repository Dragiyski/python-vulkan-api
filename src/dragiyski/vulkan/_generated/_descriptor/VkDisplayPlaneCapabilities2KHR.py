from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayPlaneCapabilities2KHR'
_member_list_ = ['sType', 'pNext', 'capabilities']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DISPLAY_PLANE_CAPABILITIES_2_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'capabilities': {
        'type': CComplexType('VkDisplayPlaneCapabilitiesKHR'),
        'type_name': 'VkDisplayPlaneCapabilitiesKHR',
        'structure': 'VkDisplayPlaneCapabilitiesKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDisplayPlaneCapabilitiesKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetDisplayPlaneCapabilities2KHR',
}
