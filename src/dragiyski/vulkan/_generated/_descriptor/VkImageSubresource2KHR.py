from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageSubresource2KHR'
_member_list_ = ['sType', 'pNext', 'imageSubresource']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_SUBRESOURCE_2_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageSubresource': {
        'type': CComplexType('VkImageSubresource'),
        'type_name': 'VkImageSubresource',
        'structure': 'VkImageSubresource',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkImageSubresource',
}
_included_in_ = {
    'VkDeviceImageSubresourceInfoKHR',
}
_input_of_ = {
    'vkGetImageSubresourceLayout2KHR',
}
_output_of_ = set()
