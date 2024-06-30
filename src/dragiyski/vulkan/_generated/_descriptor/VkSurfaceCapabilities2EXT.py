from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSurfaceCapabilities2EXT'
_member_list_ = ['sType', 'pNext', 'minImageCount', 'maxImageCount', 'currentExtent', 'minImageExtent', 'maxImageExtent', 'maxImageArrayLayers', 'supportedTransforms', 'currentTransform', 'supportedCompositeAlpha', 'supportedUsageFlags', 'supportedSurfaceCounters']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
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
    'supportedSurfaceCounters': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSurfaceCounterFlagsEXT',
        'enum': 'VkSurfaceCounterFlagsEXT',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceSurfaceCapabilities2EXT',
}
