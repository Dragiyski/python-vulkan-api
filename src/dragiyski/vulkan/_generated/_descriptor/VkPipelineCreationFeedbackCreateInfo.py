from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineCreationFeedbackCreateInfo'
_member_list_ = ['sType', 'pNext', 'pPipelineCreationFeedback', 'pipelineStageCreationFeedbackCount', 'pPipelineStageCreationFeedbacks']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_CREATION_FEEDBACK_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPipelineCreationFeedback': {
        'type': CPointerType(CComplexType('VkPipelineCreationFeedback')),
        'type_name': 'VkPipelineCreationFeedback',
        'structure': 'VkPipelineCreationFeedback',
        'is_string': False,
    },
    'pipelineStageCreationFeedbackCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPipelineStageCreationFeedbacks': {
        'type': CPointerType(CComplexType('VkPipelineCreationFeedback')),
        'type_name': 'VkPipelineCreationFeedback',
        'structure': 'VkPipelineCreationFeedback',
        'length': [['pipelineStageCreationFeedbackCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkComputePipelineCreateInfo',
    'VkExecutionGraphPipelineCreateInfoAMDX',
    'VkGraphicsPipelineCreateInfo',
    'VkRayTracingPipelineCreateInfoKHR',
    'VkRayTracingPipelineCreateInfoNV',
}
_extended_by_ = set()
_includes_ = {
    'VkPipelineCreationFeedback',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
