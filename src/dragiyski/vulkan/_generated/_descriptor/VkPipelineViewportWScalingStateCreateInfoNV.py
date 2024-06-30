from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineViewportWScalingStateCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'viewportWScalingEnable', 'viewportCount', 'pViewportWScalings']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_W_SCALING_STATE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'viewportWScalingEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'viewportCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewportWScalings': {
        'type': CPointerType(CComplexType('VkViewportWScalingNV')),
        'type_name': 'VkViewportWScalingNV',
        'structure': 'VkViewportWScalingNV',
        'length': [['viewportCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineViewportStateCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkViewportWScalingNV',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
