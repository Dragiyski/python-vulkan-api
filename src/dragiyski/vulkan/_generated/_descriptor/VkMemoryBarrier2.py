from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryBarrier2'
_member_list_ = ['sType', 'pNext', 'srcStageMask', 'srcAccessMask', 'dstStageMask', 'dstAccessMask']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MEMORY_BARRIER_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcStageMask': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkPipelineStageFlags2',
        'enum': 'VkPipelineStageFlags2',
        'is_string': False,
    },
    'srcAccessMask': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkAccessFlags2',
        'enum': 'VkAccessFlags2',
        'is_string': False,
    },
    'dstStageMask': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkPipelineStageFlags2',
        'enum': 'VkPipelineStageFlags2',
        'is_string': False,
    },
    'dstAccessMask': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkAccessFlags2',
        'enum': 'VkAccessFlags2',
        'is_string': False,
    },
}
_extends_ = {
    'VkSubpassDependency2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDependencyInfo',
}
_input_of_ = set()
_output_of_ = set()
