from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineRobustnessCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'storageBuffers', 'uniformBuffers', 'vertexInputs', 'images']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_ROBUSTNESS_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'storageBuffers': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineRobustnessBufferBehaviorEXT',
        'enum': 'VkPipelineRobustnessBufferBehaviorEXT',
        'is_string': False,
    },
    'uniformBuffers': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineRobustnessBufferBehaviorEXT',
        'enum': 'VkPipelineRobustnessBufferBehaviorEXT',
        'is_string': False,
    },
    'vertexInputs': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineRobustnessBufferBehaviorEXT',
        'enum': 'VkPipelineRobustnessBufferBehaviorEXT',
        'is_string': False,
    },
    'images': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineRobustnessImageBehaviorEXT',
        'enum': 'VkPipelineRobustnessImageBehaviorEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkComputePipelineCreateInfo',
    'VkGraphicsPipelineCreateInfo',
    'VkPipelineShaderStageCreateInfo',
    'VkRayTracingPipelineCreateInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
