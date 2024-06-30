from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubpassDependency2'
_member_list_ = ['sType', 'pNext', 'srcSubpass', 'dstSubpass', 'srcStageMask', 'dstStageMask', 'srcAccessMask', 'dstAccessMask', 'dependencyFlags', 'viewOffset']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SUBPASS_DEPENDENCY_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
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
    'viewOffset': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkMemoryBarrier2',
}
_includes_ = set()
_included_in_ = {
    'VkRenderPassCreateInfo2',
}
_input_of_ = set()
_output_of_ = set()
