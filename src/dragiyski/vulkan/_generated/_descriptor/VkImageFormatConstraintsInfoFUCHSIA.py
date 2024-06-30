from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageFormatConstraintsInfoFUCHSIA'
_member_list_ = ['sType', 'pNext', 'imageCreateInfo', 'requiredFormatFeatures', 'flags', 'sysmemPixelFormat', 'colorSpaceCount', 'pColorSpaces']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_CONSTRAINTS_INFO_FUCHSIA',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageCreateInfo': {
        'type': CComplexType('VkImageCreateInfo'),
        'type_name': 'VkImageCreateInfo',
        'structure': 'VkImageCreateInfo',
        'is_string': False,
    },
    'requiredFormatFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFormatFeatureFlags',
        'enum': 'VkFormatFeatureFlags',
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageFormatConstraintsFlagsFUCHSIA',
        'enum': 'VkImageFormatConstraintsFlagsFUCHSIA',
        'is_string': False,
    },
    'sysmemPixelFormat': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'colorSpaceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pColorSpaces': {
        'type': CPointerType(CComplexType('VkSysmemColorSpaceFUCHSIA')),
        'type_name': 'VkSysmemColorSpaceFUCHSIA',
        'structure': 'VkSysmemColorSpaceFUCHSIA',
        'length': [['colorSpaceCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkImageCreateInfo',
    'VkSysmemColorSpaceFUCHSIA',
}
_included_in_ = {
    'VkImageConstraintsInfoFUCHSIA',
}
_input_of_ = set()
_output_of_ = set()
