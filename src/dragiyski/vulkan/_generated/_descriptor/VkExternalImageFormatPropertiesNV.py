from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExternalImageFormatPropertiesNV'
_member_list_ = ['imageFormatProperties', 'externalMemoryFeatures', 'exportFromImportedHandleTypes', 'compatibleHandleTypes']
_member_info_ = {
    'imageFormatProperties': {
        'type': CComplexType('VkImageFormatProperties'),
        'type_name': 'VkImageFormatProperties',
        'structure': 'VkImageFormatProperties',
        'is_string': False,
    },
    'externalMemoryFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryFeatureFlagsNV',
        'enum': 'VkExternalMemoryFeatureFlagsNV',
        'is_string': False,
    },
    'exportFromImportedHandleTypes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryHandleTypeFlagsNV',
        'enum': 'VkExternalMemoryHandleTypeFlagsNV',
        'is_string': False,
    },
    'compatibleHandleTypes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryHandleTypeFlagsNV',
        'enum': 'VkExternalMemoryHandleTypeFlagsNV',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkImageFormatProperties',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceExternalImageFormatPropertiesNV',
}
