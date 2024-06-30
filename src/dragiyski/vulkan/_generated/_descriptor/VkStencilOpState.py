from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkStencilOpState'
_member_list_ = ['failOp', 'passOp', 'depthFailOp', 'compareOp', 'compareMask', 'writeMask', 'reference']
_member_info_ = {
    'failOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkStencilOp',
        'enum': 'VkStencilOp',
        'is_string': False,
    },
    'passOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkStencilOp',
        'enum': 'VkStencilOp',
        'is_string': False,
    },
    'depthFailOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkStencilOp',
        'enum': 'VkStencilOp',
        'is_string': False,
    },
    'compareOp': {
        'type': CIntType('c_int'),
        'type_name': 'VkCompareOp',
        'enum': 'VkCompareOp',
        'is_string': False,
    },
    'compareMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'writeMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'reference': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPipelineDepthStencilStateCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
