from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRayTracingPipelineCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'flags', 'stageCount', 'pStages', 'groupCount', 'pGroups', 'maxRecursionDepth', 'layout', 'basePipelineHandle', 'basePipelineIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineCreateFlags',
        'enum': 'VkPipelineCreateFlags',
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
    'groupCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pGroups': {
        'type': CPointerType(CComplexType('VkRayTracingShaderGroupCreateInfoNV')),
        'type_name': 'VkRayTracingShaderGroupCreateInfoNV',
        'structure': 'VkRayTracingShaderGroupCreateInfoNV',
        'length': [['groupCount']],
        'is_string': False,
    },
    'maxRecursionDepth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'basePipelineHandle': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'basePipelineIndex': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineCreateFlags2CreateInfoKHR',
    'VkPipelineCreationFeedbackCreateInfo',
}
_includes_ = {
    'VkPipelineShaderStageCreateInfo',
    'VkRayTracingShaderGroupCreateInfoNV',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateRayTracingPipelinesNV',
}
_output_of_ = set()
