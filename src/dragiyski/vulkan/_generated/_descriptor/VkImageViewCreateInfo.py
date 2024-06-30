from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageViewCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'image', 'viewType', 'format', 'components', 'subresourceRange']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageViewCreateFlags',
        'enum': 'VkImageViewCreateFlags',
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'viewType': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageViewType',
        'enum': 'VkImageViewType',
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'components': {
        'type': CComplexType('VkComponentMapping'),
        'type_name': 'VkComponentMapping',
        'structure': 'VkComponentMapping',
        'is_string': False,
    },
    'subresourceRange': {
        'type': CComplexType('VkImageSubresourceRange'),
        'type_name': 'VkImageSubresourceRange',
        'structure': 'VkImageSubresourceRange',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkExportMetalObjectCreateInfoEXT',
    'VkImageViewASTCDecodeModeEXT',
    'VkImageViewMinLodCreateInfoEXT',
    'VkImageViewSampleWeightCreateInfoQCOM',
    'VkImageViewSlicedCreateInfoEXT',
    'VkImageViewUsageCreateInfo',
    'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
    'VkSamplerYcbcrConversionInfo',
}
_includes_ = {
    'VkComponentMapping',
    'VkImageSubresourceRange',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateImageView',
}
_output_of_ = set()
