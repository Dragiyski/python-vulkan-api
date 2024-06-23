import ctypes

class CType(ctypes.Structure):
    pass

from .VkComponentMapping import CType as VkComponentMapping
from .VkImageSubresourceRange import CType as VkImageSubresourceRange

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('image', ctypes.c_void_p),
    ('viewType', ctypes.c_int),
    ('format', ctypes.c_int),
    ('components', VkComponentMapping),
    ('subresourceRange', VkImageSubresourceRange),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkExportMetalObjectCreateInfoEXT',
        'VkImageViewASTCDecodeModeEXT',
        'VkImageViewMinLodCreateInfoEXT',
        'VkImageViewSampleWeightCreateInfoQCOM',
        'VkImageViewSlicedCreateInfoEXT',
        'VkImageViewUsageCreateInfo',
        'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
        'VkSamplerYcbcrConversionInfo',
    },
    'includes': {
        'VkComponentMapping',
        'VkImageSubresourceRange',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateImageView',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkImageViewCreateFlags'},
        'image': {'python_name': ['image']},
        'viewType': {'python_name': ['view', 'type'], 'type': 'VkImageViewType'},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'components': {'python_name': ['components'], 'type': 'VkComponentMapping'},
        'subresourceRange': {'python_name': ['subresource', 'range'], 'type': 'VkImageSubresourceRange'},
    }
}
