from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkViewport'
_member_list_ = ['x', 'y', 'width', 'height', 'minDepth', 'maxDepth']
_member_info_ = {
    'x': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'y': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'width': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'height': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'minDepth': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxDepth': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkCommandBufferInheritanceViewportScissorInfoNV',
    'VkPipelineViewportStateCreateInfo',
}
_input_of_ = {
    'vkCmdSetViewport',
    'vkCmdSetViewportWithCount',
}
_output_of_ = set()
