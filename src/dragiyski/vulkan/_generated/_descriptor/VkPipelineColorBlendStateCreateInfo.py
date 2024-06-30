from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineColorBlendStateCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'logicOpEnable', 'logicOp', 'attachmentCount', 'pAttachments', 'blendConstants']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineColorBlendStateCreateFlags',
        'enum': 'VkPipelineColorBlendStateCreateFlags',
        'is_string': False,
    },
    'logicOpEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'logicOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkLogicOp',
        'enum': 'VkLogicOp',
        'is_string': False,
    },
    'attachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pAttachments': {
        'type': CPointerType(CComplexType('VkPipelineColorBlendAttachmentState')),
        'type_name': 'VkPipelineColorBlendAttachmentState',
        'structure': 'VkPipelineColorBlendAttachmentState',
        'length': [['attachmentCount']],
        'is_string': False,
    },
    'blendConstants': {
        'type': CArrayType(CFloatType('c_float'), 4),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineColorBlendAdvancedStateCreateInfoEXT',
    'VkPipelineColorWriteCreateInfoEXT',
}
_includes_ = {
    'VkPipelineColorBlendAttachmentState',
}
_included_in_ = {
    'VkGraphicsPipelineCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
