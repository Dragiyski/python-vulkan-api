from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineLayoutCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'setLayoutCount', 'pSetLayouts', 'pushConstantRangeCount', 'pPushConstantRanges']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineLayoutCreateFlags',
        'enum': 'VkPipelineLayoutCreateFlags',
        'is_string': False,
    },
    'setLayoutCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSetLayouts': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['setLayoutCount']],
        'is_string': False,
    },
    'pushConstantRangeCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPushConstantRanges': {
        'type': CPointerType(CComplexType('VkPushConstantRange')),
        'type_name': 'VkPushConstantRange',
        'structure': 'VkPushConstantRange',
        'length': [['pushConstantRangeCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkBindDescriptorBufferEmbeddedSamplersInfoEXT',
    'VkBindDescriptorSetsInfoKHR',
    'VkPushConstantsInfoKHR',
    'VkPushDescriptorSetInfoKHR',
    'VkPushDescriptorSetWithTemplateInfoKHR',
    'VkSetDescriptorBufferOffsetsInfoEXT',
}
_extended_by_ = set()
_includes_ = {
    'VkPushConstantRange',
}
_included_in_ = set()
_input_of_ = {
    'vkCreatePipelineLayout',
}
_output_of_ = set()
