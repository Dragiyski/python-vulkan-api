from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceLayeredApiVulkanPropertiesKHR'
_member_list_ = ['sType', 'pNext', 'properties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_API_VULKAN_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'properties': {
        'type': CComplexType('VkPhysicalDeviceProperties2'),
        'type_name': 'VkPhysicalDeviceProperties2',
        'structure': 'VkPhysicalDeviceProperties2',
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceLayeredApiPropertiesKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkPhysicalDeviceProperties2',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
