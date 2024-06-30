from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkColorBlendEquationEXT'
_member_list_ = ['srcColorBlendFactor', 'dstColorBlendFactor', 'colorBlendOp', 'srcAlphaBlendFactor', 'dstAlphaBlendFactor', 'alphaBlendOp']
_member_info_ = {
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
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdSetColorBlendEquationEXT',
}
_output_of_ = set()
