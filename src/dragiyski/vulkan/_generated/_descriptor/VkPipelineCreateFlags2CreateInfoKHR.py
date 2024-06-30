from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineCreateFlags2CreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_CREATE_FLAGS_2_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkPipelineCreateFlags2KHR',
        'enum': 'VkPipelineCreateFlags2KHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkComputePipelineCreateInfo',
    'VkGraphicsPipelineCreateInfo',
    'VkRayTracingPipelineCreateInfoKHR',
    'VkRayTracingPipelineCreateInfoNV',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
