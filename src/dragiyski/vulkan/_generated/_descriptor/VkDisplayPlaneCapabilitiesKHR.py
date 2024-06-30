from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayPlaneCapabilitiesKHR'
_member_list_ = ['supportedAlpha', 'minSrcPosition', 'maxSrcPosition', 'minSrcExtent', 'maxSrcExtent', 'minDstPosition', 'maxDstPosition', 'minDstExtent', 'maxDstExtent']
_member_info_ = {
    'supportedAlpha': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDisplayPlaneAlphaFlagsKHR',
        'enum': 'VkDisplayPlaneAlphaFlagsKHR',
        'is_string': False,
    },
    'minSrcPosition': {
        'type': CComplexType('VkOffset2D'),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'is_string': False,
    },
    'maxSrcPosition': {
        'type': CComplexType('VkOffset2D'),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'is_string': False,
    },
    'minSrcExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxSrcExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'minDstPosition': {
        'type': CComplexType('VkOffset2D'),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'is_string': False,
    },
    'maxDstPosition': {
        'type': CComplexType('VkOffset2D'),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'is_string': False,
    },
    'minDstExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxDstExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
    'VkOffset2D',
}
_included_in_ = {
    'VkDisplayPlaneCapabilities2KHR',
}
_input_of_ = set()
_output_of_ = {
    'vkGetDisplayPlaneCapabilitiesKHR',
}
