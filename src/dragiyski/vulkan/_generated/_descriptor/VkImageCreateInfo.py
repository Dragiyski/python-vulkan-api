from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'imageType', 'format', 'extent', 'mipLevels', 'arrayLayers', 'samples', 'tiling', 'usage', 'sharingMode', 'queueFamilyIndexCount', 'pQueueFamilyIndices', 'initialLayout']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageCreateFlags',
        'enum': 'VkImageCreateFlags',
        'is_string': False,
    },
    'imageType': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageType',
        'enum': 'VkImageType',
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'extent': {
        'type': CComplexType('VkExtent3D'),
        'type_name': 'VkExtent3D',
        'structure': 'VkExtent3D',
        'is_string': False,
    },
    'mipLevels': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'arrayLayers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'samples': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlagBits',
        'is_string': False,
    },
    'tiling': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageTiling',
        'enum': 'VkImageTiling',
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageUsageFlags',
        'enum': 'VkImageUsageFlags',
        'is_string': False,
    },
    'sharingMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkSharingMode',
        'enum': 'VkSharingMode',
        'is_string': False,
    },
    'queueFamilyIndexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pQueueFamilyIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['queueFamilyIndexCount']],
        'is_string': False,
    },
    'initialLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkBufferCollectionImageCreateInfoFUCHSIA',
    'VkDedicatedAllocationImageCreateInfoNV',
    'VkExportMetalObjectCreateInfoEXT',
    'VkExternalFormatANDROID',
    'VkExternalFormatQNX',
    'VkExternalMemoryImageCreateInfo',
    'VkExternalMemoryImageCreateInfoNV',
    'VkImageAlignmentControlCreateInfoMESA',
    'VkImageCompressionControlEXT',
    'VkImageDrmFormatModifierExplicitCreateInfoEXT',
    'VkImageDrmFormatModifierListCreateInfoEXT',
    'VkImageFormatListCreateInfo',
    'VkImageStencilUsageCreateInfo',
    'VkImageSwapchainCreateInfoKHR',
    'VkImportMetalIOSurfaceInfoEXT',
    'VkImportMetalTextureInfoEXT',
    'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
    'VkOpticalFlowImageFormatInfoNV',
    'VkVideoProfileListInfoKHR',
}
_includes_ = {
    'VkExtent3D',
}
_included_in_ = {
    'VkDeviceImageMemoryRequirements',
    'VkDeviceImageSubresourceInfoKHR',
    'VkImageFormatConstraintsInfoFUCHSIA',
}
_input_of_ = {
    'vkCreateImage',
}
_output_of_ = set()
