from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorPoolCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'maxSets', 'poolSizeCount', 'pPoolSizes']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDescriptorPoolCreateFlags',
        'enum': 'VkDescriptorPoolCreateFlags',
        'is_string': False,
    },
    'maxSets': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'poolSizeCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPoolSizes': {
        'type': CPointerType(CComplexType('VkDescriptorPoolSize')),
        'type_name': 'VkDescriptorPoolSize',
        'structure': 'VkDescriptorPoolSize',
        'length': [['poolSizeCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDescriptorPoolInlineUniformBlockCreateInfo',
    'VkMutableDescriptorTypeCreateInfoEXT',
}
_includes_ = {
    'VkDescriptorPoolSize',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateDescriptorPool',
}
_output_of_ = set()
