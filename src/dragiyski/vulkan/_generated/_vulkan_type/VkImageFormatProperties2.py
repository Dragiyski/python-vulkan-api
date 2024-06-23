import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageFormatProperties import CType as VkImageFormatProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageFormatProperties', VkImageFormatProperties),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkAndroidHardwareBufferUsageANDROID',
        'VkExternalImageFormatProperties',
        'VkFilterCubicImageViewImageFormatPropertiesEXT',
        'VkHostImageCopyDevicePerformanceQueryEXT',
        'VkImageCompressionPropertiesEXT',
        'VkSamplerYcbcrConversionImageFormatProperties',
        'VkTextureLODGatherFormatPropertiesAMD',
    },
    'includes': {
        'VkImageFormatProperties',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceImageFormatProperties2',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'imageFormatProperties': {'python_name': ['image', 'format', 'properties'], 'type': 'VkImageFormatProperties'},
    }
}
