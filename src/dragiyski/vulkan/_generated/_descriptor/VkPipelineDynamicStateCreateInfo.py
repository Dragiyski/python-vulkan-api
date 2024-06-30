from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineDynamicStateCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'dynamicStateCount', 'pDynamicStates']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_DYNAMIC_STATE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineDynamicStateCreateFlags',
        'enum': 'VkPipelineDynamicStateCreateFlags',
        'is_string': False,
    },
    'dynamicStateCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDynamicStates': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkDynamicState',
        'enum': 'VkDynamicState',
        'length': [['dynamicStateCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkGraphicsPipelineCreateInfo',
    'VkRayTracingPipelineCreateInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
