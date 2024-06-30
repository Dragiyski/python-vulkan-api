from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGraphicsShaderGroupCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'stageCount', 'pStages', 'pVertexInputState', 'pTessellationState']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_GRAPHICS_SHADER_GROUP_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stageCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStages': {
        'type': CPointerType(CComplexType('VkPipelineShaderStageCreateInfo')),
        'type_name': 'VkPipelineShaderStageCreateInfo',
        'structure': 'VkPipelineShaderStageCreateInfo',
        'length': [['stageCount']],
        'is_string': False,
    },
    'pVertexInputState': {
        'type': CPointerType(CComplexType('VkPipelineVertexInputStateCreateInfo')),
        'type_name': 'VkPipelineVertexInputStateCreateInfo',
        'structure': 'VkPipelineVertexInputStateCreateInfo',
        'is_string': False,
    },
    'pTessellationState': {
        'type': CPointerType(CComplexType('VkPipelineTessellationStateCreateInfo')),
        'type_name': 'VkPipelineTessellationStateCreateInfo',
        'structure': 'VkPipelineTessellationStateCreateInfo',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkPipelineShaderStageCreateInfo',
    'VkPipelineTessellationStateCreateInfo',
    'VkPipelineVertexInputStateCreateInfo',
}
_included_in_ = {
    'VkGraphicsPipelineShaderGroupsCreateInfoNV',
}
_input_of_ = set()
_output_of_ = set()
