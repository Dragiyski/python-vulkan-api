from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferCollectionPropertiesFUCHSIA'
_member_list_ = ['sType', 'pNext', 'memoryTypeBits', 'bufferCount', 'createInfoIndex', 'sysmemPixelFormat', 'formatFeatures', 'sysmemColorSpaceIndex', 'samplerYcbcrConversionComponents', 'suggestedYcbcrModel', 'suggestedYcbcrRange', 'suggestedXChromaOffset', 'suggestedYChromaOffset']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_COLLECTION_PROPERTIES_FUCHSIA',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryTypeBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'createInfoIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sysmemPixelFormat': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'formatFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFormatFeatureFlags',
        'enum': 'VkFormatFeatureFlags',
        'is_string': False,
    },
    'sysmemColorSpaceIndex': {
        'type': CComplexType('VkSysmemColorSpaceFUCHSIA'),
        'type_name': 'VkSysmemColorSpaceFUCHSIA',
        'structure': 'VkSysmemColorSpaceFUCHSIA',
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
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkComponentMapping',
    'VkSysmemColorSpaceFUCHSIA',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetBufferCollectionPropertiesFUCHSIA',
}
