import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineShaderStageCreateInfo import CType as VkPipelineShaderStageCreateInfo
from .VkRayTracingShaderGroupCreateInfoNV import CType as VkRayTracingShaderGroupCreateInfoNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('groupCount', ctypes.c_uint32),
    ('pGroups', ctypes.POINTER(VkRayTracingShaderGroupCreateInfoNV)),
    ('maxRecursionDepth', ctypes.c_uint32),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineCreateFlags2CreateInfoKHR',
        'VkPipelineCreationFeedbackCreateInfo',
        'VkPipelineOfflineCreateInfo',
    },
    'includes': {
        'VkPipelineShaderStageCreateInfo',
        'VkRayTracingShaderGroupCreateInfoNV',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateRayTracingPipelinesNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineCreateFlags'},
        'stageCount': {'python_name': ['stage', 'count']},
        'pStages': {'python_name': ['p', 'stages'], 'len': [['stageCount']], 'type': 'VkPipelineShaderStageCreateInfo'},
        'groupCount': {'python_name': ['group', 'count']},
        'pGroups': {'python_name': ['p', 'groups'], 'len': [['groupCount']], 'type': 'VkRayTracingShaderGroupCreateInfoNV'},
        'maxRecursionDepth': {'python_name': ['max', 'recursion', 'depth']},
        'layout': {'python_name': ['layout']},
        'basePipelineHandle': {'python_name': ['base', 'pipeline', 'handle']},
        'basePipelineIndex': {'python_name': ['base', 'pipeline', 'index']},
    }
}
