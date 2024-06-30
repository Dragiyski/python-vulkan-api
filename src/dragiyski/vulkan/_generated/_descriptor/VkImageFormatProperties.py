from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageFormatProperties'
_member_list_ = ['maxExtent', 'maxMipLevels', 'maxArrayLayers', 'sampleCounts', 'maxResourceSize']
_member_info_ = {
    'maxExtent': {
        'type': CComplexType('VkExtent3D'),
        'type_name': 'VkExtent3D',
        'structure': 'VkExtent3D',
        'is_string': False,
    },
    'maxMipLevels': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxArrayLayers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sampleCounts': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlags',
        'enum': 'VkSampleCountFlags',
        'is_string': False,
    },
    'maxResourceSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent3D',
}
_included_in_ = {
    'VkExternalImageFormatPropertiesNV',
    'VkImageFormatProperties2',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceImageFormatProperties',
}
