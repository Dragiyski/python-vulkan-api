from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkComputePipelineCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'stage', 'layout', 'basePipelineHandle', 'basePipelineIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_CREATE_INFO',
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
    'stage': {
        'type': CComplexType('VkPipelineShaderStageCreateInfo'),
        'type_name': 'VkPipelineShaderStageCreateInfo',
        'structure': 'VkPipelineShaderStageCreateInfo',
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
    'VkComputePipelineIndirectBufferInfoNV',
    'VkPipelineCompilerControlCreateInfoAMD',
    'VkPipelineCreateFlags2CreateInfoKHR',
    'VkPipelineCreationFeedbackCreateInfo',
    'VkPipelineRobustnessCreateInfoEXT',
    'VkSubpassShadingPipelineCreateInfoHUAWEI',
}
_includes_ = {
    'VkPipelineShaderStageCreateInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateComputePipelines',
    'vkGetPipelineIndirectMemoryRequirementsNV',
}
_output_of_ = set()
