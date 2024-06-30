from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineDepthStencilStateCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'depthTestEnable', 'depthWriteEnable', 'depthCompareOp', 'depthBoundsTestEnable', 'stencilTestEnable', 'front', 'back', 'minDepthBounds', 'maxDepthBounds']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_DEPTH_STENCIL_STATE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineDepthStencilStateCreateFlags',
        'enum': 'VkPipelineDepthStencilStateCreateFlags',
        'is_string': False,
    },
    'depthTestEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'depthWriteEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'depthCompareOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkCompareOp',
        'enum': 'VkCompareOp',
        'is_string': False,
    },
    'depthBoundsTestEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stencilTestEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'front': {
        'type': CComplexType('VkStencilOpState'),
        'type_name': 'VkStencilOpState',
        'structure': 'VkStencilOpState',
        'is_string': False,
    },
    'back': {
        'type': CComplexType('VkStencilOpState'),
        'type_name': 'VkStencilOpState',
        'structure': 'VkStencilOpState',
        'is_string': False,
    },
    'minDepthBounds': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxDepthBounds': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkStencilOpState',
}
_included_in_ = {
    'VkGraphicsPipelineCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
