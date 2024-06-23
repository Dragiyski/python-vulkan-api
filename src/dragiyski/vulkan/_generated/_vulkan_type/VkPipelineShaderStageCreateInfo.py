import ctypes

class CType(ctypes.Structure):
    pass

from .VkSpecializationInfo import CType as VkSpecializationInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', ctypes.c_uint32),
    ('module', ctypes.c_void_p),
    ('pName', ctypes.c_char_p),
    ('pSpecializationInfo', ctypes.POINTER(VkSpecializationInfo)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDebugUtilsObjectNameInfoEXT',
        'VkPipelineRobustnessCreateInfoEXT',
        'VkPipelineShaderStageModuleIdentifierCreateInfoEXT',
        'VkPipelineShaderStageNodeCreateInfoAMDX',
        'VkPipelineShaderStageRequiredSubgroupSizeCreateInfo',
        'VkShaderModuleCreateInfo',
        'VkShaderModuleValidationCacheCreateInfoEXT',
    },
    'includes': {
        'VkSpecializationInfo',
    },
    'included_in': {
        'VkComputePipelineCreateInfo',
        'VkExecutionGraphPipelineCreateInfoAMDX',
        'VkGraphicsPipelineCreateInfo',
        'VkGraphicsShaderGroupCreateInfoNV',
        'VkRayTracingPipelineCreateInfoKHR',
        'VkRayTracingPipelineCreateInfoNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineShaderStageCreateFlags'},
        'stage': {'python_name': ['stage'], 'type': 'VkShaderStageFlagBits'},
        'module': {'python_name': ['module']},
        'pName': {'python_name': ['p', 'name'], 'len': [['null-terminated']]},
        'pSpecializationInfo': {'python_name': ['p', 'specialization', 'info'], 'type': 'VkSpecializationInfo'},
    }
}
