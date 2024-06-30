from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorSetVariableDescriptorCountAllocateInfo'
_member_list_ = ['sType', 'pNext', 'descriptorSetCount', 'pDescriptorCounts']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_ALLOCATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'descriptorSetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDescriptorCounts': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['descriptorSetCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkDescriptorSetAllocateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
