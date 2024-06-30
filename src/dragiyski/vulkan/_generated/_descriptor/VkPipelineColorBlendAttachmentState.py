from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineColorBlendAttachmentState'
_member_list_ = ['blendEnable', 'srcColorBlendFactor', 'dstColorBlendFactor', 'colorBlendOp', 'srcAlphaBlendFactor', 'dstAlphaBlendFactor', 'alphaBlendOp', 'colorWriteMask']
_member_info_ = {
    'blendEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'srcColorBlendFactor': {
        'type': CIntType('c_int'),
        'type_name': 'VkBlendFactor',
        'enum': 'VkBlendFactor',
        'is_string': False,
    },
    'dstColorBlendFactor': {
        'type': CIntType('c_int'),
        'type_name': 'VkBlendFactor',
        'enum': 'VkBlendFactor',
        'is_string': False,
    },
    'colorBlendOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkBlendOp',
        'enum': 'VkBlendOp',
        'is_string': False,
    },
    'srcAlphaBlendFactor': {
        'type': CIntType('c_int'),
        'type_name': 'VkBlendFactor',
        'enum': 'VkBlendFactor',
        'is_string': False,
    },
    'dstAlphaBlendFactor': {
        'type': CIntType('c_int'),
        'type_name': 'VkBlendFactor',
        'enum': 'VkBlendFactor',
        'is_string': False,
    },
    'alphaBlendOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkBlendOp',
        'enum': 'VkBlendOp',
        'is_string': False,
    },
    'colorWriteMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkColorComponentFlags',
        'enum': 'VkColorComponentFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPipelineColorBlendStateCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
