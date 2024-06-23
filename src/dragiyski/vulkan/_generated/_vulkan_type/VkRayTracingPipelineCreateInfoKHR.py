import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineDynamicStateCreateInfo import CType as VkPipelineDynamicStateCreateInfo
from .VkPipelineLibraryCreateInfoKHR import CType as VkPipelineLibraryCreateInfoKHR
from .VkPipelineShaderStageCreateInfo import CType as VkPipelineShaderStageCreateInfo
from .VkRayTracingPipelineInterfaceCreateInfoKHR import CType as VkRayTracingPipelineInterfaceCreateInfoKHR
from .VkRayTracingShaderGroupCreateInfoKHR import CType as VkRayTracingShaderGroupCreateInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('groupCount', ctypes.c_uint32),
    ('pGroups', ctypes.POINTER(VkRayTracingShaderGroupCreateInfoKHR)),
    ('maxPipelineRayRecursionDepth', ctypes.c_uint32),
    ('pLibraryInfo', ctypes.POINTER(VkPipelineLibraryCreateInfoKHR)),
    ('pLibraryInterface', ctypes.POINTER(VkRayTracingPipelineInterfaceCreateInfoKHR)),
    ('pDynamicState', ctypes.POINTER(VkPipelineDynamicStateCreateInfo)),
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
        'VkPipelineRobustnessCreateInfoEXT',
    },
    'includes': {
        'VkPipelineDynamicStateCreateInfo',
        'VkPipelineLibraryCreateInfoKHR',
        'VkPipelineShaderStageCreateInfo',
        'VkRayTracingPipelineInterfaceCreateInfoKHR',
        'VkRayTracingShaderGroupCreateInfoKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateRayTracingPipelinesKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineCreateFlags'},
        'stageCount': {'python_name': ['stage', 'count']},
        'pStages': {'python_name': ['p', 'stages'], 'len': [['stageCount']], 'type': 'VkPipelineShaderStageCreateInfo'},
        'groupCount': {'python_name': ['group', 'count']},
        'pGroups': {'python_name': ['p', 'groups'], 'len': [['groupCount']], 'type': 'VkRayTracingShaderGroupCreateInfoKHR'},
        'maxPipelineRayRecursionDepth': {'python_name': ['max', 'pipeline', 'ray', 'recursion', 'depth']},
        'pLibraryInfo': {'python_name': ['p', 'library', 'info'], 'type': 'VkPipelineLibraryCreateInfoKHR'},
        'pLibraryInterface': {'python_name': ['p', 'library', 'interface'], 'type': 'VkRayTracingPipelineInterfaceCreateInfoKHR'},
        'pDynamicState': {'python_name': ['p', 'dynamic', 'state'], 'type': 'VkPipelineDynamicStateCreateInfo'},
        'layout': {'python_name': ['layout']},
        'basePipelineHandle': {'python_name': ['base', 'pipeline', 'handle']},
        'basePipelineIndex': {'python_name': ['base', 'pipeline', 'index']},
    }
}
