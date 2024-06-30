from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRayTracingPipelineCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'stageCount', 'pStages', 'groupCount', 'pGroups', 'maxPipelineRayRecursionDepth', 'pLibraryInfo', 'pLibraryInterface', 'pDynamicState', 'layout', 'basePipelineHandle', 'basePipelineIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_KHR',
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
        'type': CPointerType(CComplexType('VkRayTracingShaderGroupCreateInfoKHR')),
        'type_name': 'VkRayTracingShaderGroupCreateInfoKHR',
        'structure': 'VkRayTracingShaderGroupCreateInfoKHR',
        'length': [['groupCount']],
        'is_string': False,
    },
    'maxPipelineRayRecursionDepth': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pLibraryInfo': {
        'type': CPointerType(CComplexType('VkPipelineLibraryCreateInfoKHR')),
        'type_name': 'VkPipelineLibraryCreateInfoKHR',
        'structure': 'VkPipelineLibraryCreateInfoKHR',
        'is_string': False,
    },
    'pLibraryInterface': {
        'type': CPointerType(CComplexType('VkRayTracingPipelineInterfaceCreateInfoKHR')),
        'type_name': 'VkRayTracingPipelineInterfaceCreateInfoKHR',
        'structure': 'VkRayTracingPipelineInterfaceCreateInfoKHR',
        'is_string': False,
    },
    'pDynamicState': {
        'type': CPointerType(CComplexType('VkPipelineDynamicStateCreateInfo')),
        'type_name': 'VkPipelineDynamicStateCreateInfo',
        'structure': 'VkPipelineDynamicStateCreateInfo',
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
    'VkPipelineRobustnessCreateInfoEXT',
}
_includes_ = {
    'VkPipelineDynamicStateCreateInfo',
    'VkPipelineLibraryCreateInfoKHR',
    'VkPipelineShaderStageCreateInfo',
    'VkRayTracingPipelineInterfaceCreateInfoKHR',
    'VkRayTracingShaderGroupCreateInfoKHR',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateRayTracingPipelinesKHR',
}
_output_of_ = set()
