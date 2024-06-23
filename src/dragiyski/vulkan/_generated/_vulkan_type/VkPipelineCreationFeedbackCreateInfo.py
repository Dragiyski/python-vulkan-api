import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineCreationFeedback import CType as VkPipelineCreationFeedback

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pPipelineCreationFeedback', ctypes.POINTER(VkPipelineCreationFeedback)),
    ('pipelineStageCreationFeedbackCount', ctypes.c_uint32),
    ('pPipelineStageCreationFeedbacks', ctypes.POINTER(VkPipelineCreationFeedback)),
]

descriptor = {
    'extends': {
        'VkComputePipelineCreateInfo',
        'VkExecutionGraphPipelineCreateInfoAMDX',
        'VkGraphicsPipelineCreateInfo',
        'VkRayTracingPipelineCreateInfoKHR',
        'VkRayTracingPipelineCreateInfoNV',
    },
    'extended_by': set(),
    'includes': {
        'VkPipelineCreationFeedback',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_CREATION_FEEDBACK_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pPipelineCreationFeedback': {'python_name': ['p', 'pipeline', 'creation', 'feedback'], 'type': 'VkPipelineCreationFeedback'},
        'pipelineStageCreationFeedbackCount': {'python_name': ['pipeline', 'stage', 'creation', 'feedback', 'count']},
        'pPipelineStageCreationFeedbacks': {'python_name': ['p', 'pipeline', 'stage', 'creation', 'feedbacks'], 'len': [['pipelineStageCreationFeedbackCount']], 'type': 'VkPipelineCreationFeedback'},
    }
}
