from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorSetLayoutCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'bindingCount', 'pBindings']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDescriptorSetLayoutCreateFlags',
        'enum': 'VkDescriptorSetLayoutCreateFlags',
        'is_string': False,
    },
    'bindingCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBindings': {
        'type': CPointerType(CComplexType('VkDescriptorSetLayoutBinding')),
        'type_name': 'VkDescriptorSetLayoutBinding',
        'structure': 'VkDescriptorSetLayoutBinding',
        'length': [['bindingCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDescriptorSetLayoutBindingFlagsCreateInfo',
    'VkMutableDescriptorTypeCreateInfoEXT',
}
_includes_ = {
    'VkDescriptorSetLayoutBinding',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateDescriptorSetLayout',
    'vkGetDescriptorSetLayoutSupport',
}
_output_of_ = set()
