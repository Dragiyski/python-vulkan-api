from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkFormatProperties'
_member_list_ = ['linearTilingFeatures', 'optimalTilingFeatures', 'bufferFeatures']
_member_info_ = {
    'linearTilingFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFormatFeatureFlags',
        'enum': 'VkFormatFeatureFlags',
        'is_string': False,
    },
    'optimalTilingFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFormatFeatureFlags',
        'enum': 'VkFormatFeatureFlags',
        'is_string': False,
    },
    'bufferFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFormatFeatureFlags',
        'enum': 'VkFormatFeatureFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkFormatProperties2',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceFormatProperties',
}
