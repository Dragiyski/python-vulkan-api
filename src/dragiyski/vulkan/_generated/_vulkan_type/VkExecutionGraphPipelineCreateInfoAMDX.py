import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineLibraryCreateInfoKHR import CType as VkPipelineLibraryCreateInfoKHR
from .VkPipelineShaderStageCreateInfo import CType as VkPipelineShaderStageCreateInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('pLibraryInfo', ctypes.POINTER(VkPipelineLibraryCreateInfoKHR)),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineCompilerControlCreateInfoAMD',
        'VkPipelineCreationFeedbackCreateInfo',
    },
    'includes': {
        'VkPipelineLibraryCreateInfoKHR',
        'VkPipelineShaderStageCreateInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateExecutionGraphPipelinesAMDX',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXECUTION_GRAPH_PIPELINE_CREATE_INFO_AMDX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineCreateFlags'},
        'stageCount': {'python_name': ['stage', 'count']},
        'pStages': {'python_name': ['p', 'stages'], 'len': [['stageCount']], 'type': 'VkPipelineShaderStageCreateInfo'},
        'pLibraryInfo': {'python_name': ['p', 'library', 'info'], 'type': 'VkPipelineLibraryCreateInfoKHR'},
        'layout': {'python_name': ['layout']},
        'basePipelineHandle': {'python_name': ['base', 'pipeline', 'handle']},
        'basePipelineIndex': {'python_name': ['base', 'pipeline', 'index']},
    }
}
