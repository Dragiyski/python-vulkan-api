from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAndroidHardwareBufferFormatProperties2ANDROID'
_member_list_ = ['sType', 'pNext', 'format', 'externalFormat', 'formatFeatures', 'samplerYcbcrConversionComponents', 'suggestedYcbcrModel', 'suggestedYcbcrRange', 'suggestedXChromaOffset', 'suggestedYChromaOffset']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_PROPERTIES_2_ANDROID',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'externalFormat': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'formatFeatures': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkFormatFeatureFlags2',
        'enum': 'VkFormatFeatureFlags2',
        'is_string': False,
    },
    'samplerYcbcrConversionComponents': {
        'type': CComplexType('VkComponentMapping'),
        'type_name': 'VkComponentMapping',
        'structure': 'VkComponentMapping',
        'is_string': False,
    },
    'suggestedYcbcrModel': {
        'type': CIntType('c_int'),
        'type_name': 'VkSamplerYcbcrModelConversion',
        'enum': 'VkSamplerYcbcrModelConversion',
        'is_string': False,
    },
    'suggestedYcbcrRange': {
        'type': CIntType('c_int'),
        'type_name': 'VkSamplerYcbcrRange',
        'enum': 'VkSamplerYcbcrRange',
        'is_string': False,
    },
    'suggestedXChromaOffset': {
        'type': CIntType('c_int'),
        'type_name': 'VkChromaLocation',
        'enum': 'VkChromaLocation',
        'is_string': False,
    },
    'suggestedYChromaOffset': {
        'type': CIntType('c_int'),
        'type_name': 'VkChromaLocation',
        'enum': 'VkChromaLocation',
        'is_string': False,
    },
}
_extends_ = {
    'VkAndroidHardwareBufferPropertiesANDROID',
}
_extended_by_ = set()
_includes_ = {
    'VkComponentMapping',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
