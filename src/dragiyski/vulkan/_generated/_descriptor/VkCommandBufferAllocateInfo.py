from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCommandBufferAllocateInfo'
_member_list_ = ['sType', 'pNext', 'commandPool', 'level', 'commandBufferCount']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'commandPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'level': {
        'type': CIntType('c_int'),
        'type_name': 'VkCommandBufferLevel',
        'enum': 'VkCommandBufferLevel',
        'is_string': False,
    },
    'commandBufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkAllocateCommandBuffers',
}
_output_of_ = set()
