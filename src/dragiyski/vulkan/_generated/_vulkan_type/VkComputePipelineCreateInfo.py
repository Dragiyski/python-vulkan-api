import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineShaderStageCreateInfo import CType as VkPipelineShaderStageCreateInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', VkPipelineShaderStageCreateInfo),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkComputePipelineIndirectBufferInfoNV',
        'VkPipelineCompilerControlCreateInfoAMD',
        'VkPipelineCreateFlags2CreateInfoKHR',
        'VkPipelineCreationFeedbackCreateInfo',
        'VkPipelineOfflineCreateInfo',
        'VkPipelineRobustnessCreateInfoEXT',
        'VkSubpassShadingPipelineCreateInfoHUAWEI',
    },
    'includes': {
        'VkPipelineShaderStageCreateInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateComputePipelines',
        'vkGetPipelineIndirectMemoryRequirementsNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineCreateFlags'},
        'stage': {'python_name': ['stage'], 'type': 'VkPipelineShaderStageCreateInfo'},
        'layout': {'python_name': ['layout']},
        'basePipelineHandle': {'python_name': ['base', 'pipeline', 'handle']},
        'basePipelineIndex': {'python_name': ['base', 'pipeline', 'index']},
    }
}
