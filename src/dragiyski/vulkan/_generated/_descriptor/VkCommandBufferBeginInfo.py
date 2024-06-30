from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCommandBufferBeginInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'pInheritanceInfo']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkCommandBufferUsageFlags',
        'enum': 'VkCommandBufferUsageFlags',
        'is_string': False,
    },
    'pInheritanceInfo': {
        'type': CPointerType(CComplexType('VkCommandBufferInheritanceInfo')),
        'type_name': 'VkCommandBufferInheritanceInfo',
        'structure': 'VkCommandBufferInheritanceInfo',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDeviceGroupCommandBufferBeginInfo',
}
_includes_ = {
    'VkCommandBufferInheritanceInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkBeginCommandBuffer',
}
_output_of_ = set()
