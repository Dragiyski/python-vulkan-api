from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSparseImageFormatProperties'
_member_list_ = ['aspectMask', 'imageGranularity', 'flags']
_member_info_ = {
    'aspectMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageAspectFlags',
        'enum': 'VkImageAspectFlags',
        'is_string': False,
    },
    'imageGranularity': {
        'type': CComplexType('VkExtent3D'),
        'type_name': 'VkExtent3D',
        'structure': 'VkExtent3D',
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSparseImageFormatFlags',
        'enum': 'VkSparseImageFormatFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent3D',
}
_included_in_ = {
    'VkSparseImageFormatProperties2',
    'VkSparseImageMemoryRequirements',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceSparseImageFormatProperties',
}
