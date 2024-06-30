from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageMemoryBarrier2'
_member_list_ = ['sType', 'pNext', 'srcStageMask', 'srcAccessMask', 'dstStageMask', 'dstAccessMask', 'oldLayout', 'newLayout', 'srcQueueFamilyIndex', 'dstQueueFamilyIndex', 'image', 'subresourceRange']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER_2',
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
    'oldLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'newLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'srcQueueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dstQueueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'subresourceRange': {
        'type': CComplexType('VkImageSubresourceRange'),
        'type_name': 'VkImageSubresourceRange',
        'structure': 'VkImageSubresourceRange',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkExternalMemoryAcquireUnmodifiedEXT',
    'VkSampleLocationsInfoEXT',
}
_includes_ = {
    'VkImageSubresourceRange',
}
_included_in_ = {
    'VkDependencyInfo',
}
_input_of_ = set()
_output_of_ = set()
