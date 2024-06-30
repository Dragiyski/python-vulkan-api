from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineViewportStateCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'viewportCount', 'pViewports', 'scissorCount', 'pScissors']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineViewportStateCreateFlags',
        'enum': 'VkPipelineViewportStateCreateFlags',
        'is_string': False,
    },
    'viewportCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pViewports': {
        'type': CPointerType(CComplexType('VkViewport')),
        'type_name': 'VkViewport',
        'structure': 'VkViewport',
        'length': [['viewportCount']],
        'is_string': False,
    },
    'scissorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pScissors': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'length': [['scissorCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineViewportCoarseSampleOrderStateCreateInfoNV',
    'VkPipelineViewportDepthClipControlCreateInfoEXT',
    'VkPipelineViewportExclusiveScissorStateCreateInfoNV',
    'VkPipelineViewportShadingRateImageStateCreateInfoNV',
    'VkPipelineViewportSwizzleStateCreateInfoNV',
    'VkPipelineViewportWScalingStateCreateInfoNV',
}
_includes_ = {
    'VkRect2D',
    'VkViewport',
}
_included_in_ = {
    'VkGraphicsPipelineCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
