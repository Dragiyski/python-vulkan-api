from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubpassDependency'
_member_list_ = ['srcSubpass', 'dstSubpass', 'srcStageMask', 'dstStageMask', 'srcAccessMask', 'dstAccessMask', 'dependencyFlags']
_member_info_ = {
    'srcSubpass': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dstSubpass': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'srcStageMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineStageFlags',
        'enum': 'VkPipelineStageFlags',
        'is_string': False,
    },
    'dstStageMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineStageFlags',
        'enum': 'VkPipelineStageFlags',
        'is_string': False,
    },
    'srcAccessMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkAccessFlags',
        'enum': 'VkAccessFlags',
        'is_string': False,
    },
    'dstAccessMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkAccessFlags',
        'enum': 'VkAccessFlags',
        'is_string': False,
    },
    'dependencyFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDependencyFlags',
        'enum': 'VkDependencyFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkRenderPassCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
