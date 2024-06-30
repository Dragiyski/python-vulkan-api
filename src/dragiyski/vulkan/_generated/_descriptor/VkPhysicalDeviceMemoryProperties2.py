from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceMemoryProperties2'
_member_list_ = ['sType', 'pNext', 'memoryProperties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PROPERTIES_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryProperties': {
        'type': CComplexType('VkPhysicalDeviceMemoryProperties'),
        'type_name': 'VkPhysicalDeviceMemoryProperties',
        'structure': 'VkPhysicalDeviceMemoryProperties',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPhysicalDeviceMemoryBudgetPropertiesEXT',
}
_includes_ = {
    'VkPhysicalDeviceMemoryProperties',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceMemoryProperties2',
}
