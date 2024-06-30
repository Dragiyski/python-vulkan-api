from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSurfaceCapabilitiesKHR'
_member_list_ = ['minImageCount', 'maxImageCount', 'currentExtent', 'minImageExtent', 'maxImageExtent', 'maxImageArrayLayers', 'supportedTransforms', 'currentTransform', 'supportedCompositeAlpha', 'supportedUsageFlags']
_member_info_ = {
    'minImageCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxImageCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'currentExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'minImageExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxImageExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxImageArrayLayers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'supportedTransforms': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSurfaceTransformFlagsKHR',
        'enum': 'VkSurfaceTransformFlagsKHR',
        'is_string': False,
    },
    'currentTransform': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSurfaceTransformFlagBitsKHR',
        'is_string': False,
    },
    'supportedCompositeAlpha': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkCompositeAlphaFlagsKHR',
        'enum': 'VkCompositeAlphaFlagsKHR',
        'is_string': False,
    },
    'supportedUsageFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageUsageFlags',
        'enum': 'VkImageUsageFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = {
    'VkSurfaceCapabilities2KHR',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceSurfaceCapabilitiesKHR',
}
