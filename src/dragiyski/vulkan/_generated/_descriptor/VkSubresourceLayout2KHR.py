from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubresourceLayout2KHR'
_member_list_ = ['sType', 'pNext', 'subresourceLayout']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SUBRESOURCE_LAYOUT_2_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'subresourceLayout': {
        'type': CComplexType('VkSubresourceLayout'),
        'type_name': 'VkSubresourceLayout',
        'structure': 'VkSubresourceLayout',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkImageCompressionPropertiesEXT',
    'VkSubresourceHostMemcpySizeEXT',
}
_includes_ = {
    'VkSubresourceLayout',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetDeviceImageSubresourceLayoutKHR',
    'vkGetImageSubresourceLayout2KHR',
}
