from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBindDescriptorSetsInfoKHR'
_member_list_ = ['sType', 'pNext', 'stageFlags', 'layout', 'firstSet', 'descriptorSetCount', 'pDescriptorSets', 'dynamicOffsetCount', 'pDynamicOffsets']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BIND_DESCRIPTOR_SETS_INFO_KHR',
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
    'firstSet': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorSetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDescriptorSets': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['descriptorSetCount']],
        'is_string': False,
    },
    'dynamicOffsetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDynamicOffsets': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['dynamicOffsetCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineLayoutCreateInfo',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdBindDescriptorSets2KHR',
}
_output_of_ = set()
