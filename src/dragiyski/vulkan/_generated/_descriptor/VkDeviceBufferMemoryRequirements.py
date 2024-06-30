from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceBufferMemoryRequirements'
_member_list_ = ['sType', 'pNext', 'pCreateInfo']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_BUFFER_MEMORY_REQUIREMENTS',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkBufferCreateInfo')),
        'type_name': 'VkBufferCreateInfo',
        'structure': 'VkBufferCreateInfo',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkBufferCreateInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkGetDeviceBufferMemoryRequirements',
}
_output_of_ = set()
