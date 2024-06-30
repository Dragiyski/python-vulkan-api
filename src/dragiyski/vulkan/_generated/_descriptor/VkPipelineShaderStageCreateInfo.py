from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineShaderStageCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'stage', 'module', 'pName', 'pSpecializationInfo']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineShaderStageCreateFlags',
        'enum': 'VkPipelineShaderStageCreateFlags',
        'is_string': False,
    },
    'stage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlagBits',
        'is_string': False,
    },
    'module': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'pSpecializationInfo': {
        'type': CPointerType(CComplexType('VkSpecializationInfo')),
        'type_name': 'VkSpecializationInfo',
        'structure': 'VkSpecializationInfo',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDebugUtilsObjectNameInfoEXT',
    'VkPipelineRobustnessCreateInfoEXT',
    'VkPipelineShaderStageModuleIdentifierCreateInfoEXT',
    'VkPipelineShaderStageNodeCreateInfoAMDX',
    'VkPipelineShaderStageRequiredSubgroupSizeCreateInfo',
    'VkShaderModuleCreateInfo',
    'VkShaderModuleValidationCacheCreateInfoEXT',
}
_includes_ = {
    'VkSpecializationInfo',
}
_included_in_ = {
    'VkComputePipelineCreateInfo',
    'VkExecutionGraphPipelineCreateInfoAMDX',
    'VkGraphicsPipelineCreateInfo',
    'VkGraphicsShaderGroupCreateInfoNV',
    'VkRayTracingPipelineCreateInfoKHR',
    'VkRayTracingPipelineCreateInfoNV',
}
_input_of_ = set()
_output_of_ = set()
