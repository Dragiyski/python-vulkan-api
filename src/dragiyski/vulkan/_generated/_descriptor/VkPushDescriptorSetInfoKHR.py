from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPushDescriptorSetInfoKHR'
_member_list_ = ['sType', 'pNext', 'stageFlags', 'layout', 'set', 'descriptorWriteCount', 'pDescriptorWrites']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PUSH_DESCRIPTOR_SET_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stageFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'set': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorWriteCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDescriptorWrites': {
        'type': CPointerType(CComplexType('VkWriteDescriptorSet')),
        'type_name': 'VkWriteDescriptorSet',
        'structure': 'VkWriteDescriptorSet',
        'length': [['descriptorWriteCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineLayoutCreateInfo',
}
_includes_ = {
    'VkWriteDescriptorSet',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdPushDescriptorSet2KHR',
}
_output_of_ = set()
