from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceImageSubresourceInfoKHR'
_member_list_ = ['sType', 'pNext', 'pCreateInfo', 'pSubresource']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_IMAGE_SUBRESOURCE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkImageCreateInfo')),
        'type_name': 'VkImageCreateInfo',
        'structure': 'VkImageCreateInfo',
        'is_string': False,
    },
    'pSubresource': {
        'type': CPointerType(CComplexType('VkImageSubresource2KHR')),
        'type_name': 'VkImageSubresource2KHR',
        'structure': 'VkImageSubresource2KHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkImageCreateInfo',
    'VkImageSubresource2KHR',
}
_included_in_ = set()
_input_of_ = {
    'vkGetDeviceImageSubresourceLayoutKHR',
}
_output_of_ = set()
