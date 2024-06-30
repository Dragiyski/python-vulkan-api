from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorSetAllocateInfo'
_member_list_ = ['sType', 'pNext', 'descriptorPool', 'descriptorSetCount', 'pSetLayouts']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_ALLOCATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorSetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSetLayouts': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['descriptorSetCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDescriptorSetVariableDescriptorCountAllocateInfo',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkAllocateDescriptorSets',
}
_output_of_ = set()
