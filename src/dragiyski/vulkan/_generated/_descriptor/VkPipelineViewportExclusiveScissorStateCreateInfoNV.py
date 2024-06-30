from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineViewportExclusiveScissorStateCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'exclusiveScissorCount', 'pExclusiveScissors']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_EXCLUSIVE_SCISSOR_STATE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'exclusiveScissorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pExclusiveScissors': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'length': [['exclusiveScissorCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineViewportStateCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkRect2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
