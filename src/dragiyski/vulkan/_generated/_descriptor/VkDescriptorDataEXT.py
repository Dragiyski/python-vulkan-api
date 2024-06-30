from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkDescriptorDataEXT'
_member_list_ = ['pSampler', 'pCombinedImageSampler', 'pInputAttachmentImage', 'pSampledImage', 'pStorageImage', 'pUniformTexelBuffer', 'pStorageTexelBuffer', 'pUniformBuffer', 'pStorageBuffer', 'accelerationStructure']
_member_info_ = {
    'pSampler': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
    'pCombinedImageSampler': {
        'type': CPointerType(CComplexType('VkDescriptorImageInfo')),
        'type_name': 'VkDescriptorImageInfo',
        'structure': 'VkDescriptorImageInfo',
        'is_string': False,
    },
    'pInputAttachmentImage': {
        'type': CPointerType(CComplexType('VkDescriptorImageInfo')),
        'type_name': 'VkDescriptorImageInfo',
        'structure': 'VkDescriptorImageInfo',
        'is_string': False,
    },
    'pSampledImage': {
        'type': CPointerType(CComplexType('VkDescriptorImageInfo')),
        'type_name': 'VkDescriptorImageInfo',
        'structure': 'VkDescriptorImageInfo',
        'is_string': False,
    },
    'pStorageImage': {
        'type': CPointerType(CComplexType('VkDescriptorImageInfo')),
        'type_name': 'VkDescriptorImageInfo',
        'structure': 'VkDescriptorImageInfo',
        'is_string': False,
    },
    'pUniformTexelBuffer': {
        'type': CPointerType(CComplexType('VkDescriptorAddressInfoEXT')),
        'type_name': 'VkDescriptorAddressInfoEXT',
        'structure': 'VkDescriptorAddressInfoEXT',
        'is_string': False,
    },
    'pStorageTexelBuffer': {
        'type': CPointerType(CComplexType('VkDescriptorAddressInfoEXT')),
        'type_name': 'VkDescriptorAddressInfoEXT',
        'structure': 'VkDescriptorAddressInfoEXT',
        'is_string': False,
    },
    'pUniformBuffer': {
        'type': CPointerType(CComplexType('VkDescriptorAddressInfoEXT')),
        'type_name': 'VkDescriptorAddressInfoEXT',
        'structure': 'VkDescriptorAddressInfoEXT',
        'is_string': False,
    },
    'pStorageBuffer': {
        'type': CPointerType(CComplexType('VkDescriptorAddressInfoEXT')),
        'type_name': 'VkDescriptorAddressInfoEXT',
        'structure': 'VkDescriptorAddressInfoEXT',
        'is_string': False,
    },
    'accelerationStructure': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDescriptorAddressInfoEXT',
    'VkDescriptorImageInfo',
}
_included_in_ = {
    'VkDescriptorGetInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
