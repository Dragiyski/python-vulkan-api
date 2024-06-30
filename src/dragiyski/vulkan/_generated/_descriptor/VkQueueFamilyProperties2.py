from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkQueueFamilyProperties2'
_member_list_ = ['sType', 'pNext', 'queueFamilyProperties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_PROPERTIES_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queueFamilyProperties': {
        'type': CComplexType('VkQueueFamilyProperties'),
        'type_name': 'VkQueueFamilyProperties',
        'structure': 'VkQueueFamilyProperties',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkQueueFamilyCheckpointProperties2NV',
    'VkQueueFamilyCheckpointPropertiesNV',
    'VkQueueFamilyGlobalPriorityPropertiesKHR',
    'VkQueueFamilyQueryResultStatusPropertiesKHR',
    'VkQueueFamilyVideoPropertiesKHR',
}
_includes_ = {
    'VkQueueFamilyProperties',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceQueueFamilyProperties2',
}
