import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('imageType', ctypes.c_int),
    ('format', ctypes.c_int),
    ('extent', VkExtent3D),
    ('mipLevels', ctypes.c_uint32),
    ('arrayLayers', ctypes.c_uint32),
    ('samples', ctypes.c_uint32),
    ('tiling', ctypes.c_int),
    ('usage', ctypes.c_uint32),
    ('sharingMode', ctypes.c_int),
    ('queueFamilyIndexCount', ctypes.c_uint32),
    ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ('initialLayout', ctypes.c_int),
]

descriptor = {
    'extends': set(),
    'extended_by': {
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
    },
    'includes': {
        'VkExtent3D',
    },
    'included_in': {
        'VkDeviceImageMemoryRequirements',
        'VkDeviceImageSubresourceInfoKHR',
        'VkImageFormatConstraintsInfoFUCHSIA',
    },
    'input_of': {
        'vkCreateImage',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkImageCreateFlags'},
        'imageType': {'python_name': ['image', 'type'], 'type': 'VkImageType'},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'extent': {'python_name': ['extent'], 'type': 'VkExtent3D'},
        'mipLevels': {'python_name': ['mip', 'levels']},
        'arrayLayers': {'python_name': ['array', 'layers']},
        'samples': {'python_name': ['samples'], 'type': 'VkSampleCountFlagBits'},
        'tiling': {'python_name': ['tiling'], 'type': 'VkImageTiling'},
        'usage': {'python_name': ['usage'], 'type': 'VkImageUsageFlags'},
        'sharingMode': {'python_name': ['sharing', 'mode'], 'type': 'VkSharingMode'},
        'queueFamilyIndexCount': {'python_name': ['queue', 'family', 'index', 'count']},
        'pQueueFamilyIndices': {'python_name': ['p', 'queue', 'family', 'indices'], 'len': [['queueFamilyIndexCount']]},
        'initialLayout': {'python_name': ['initial', 'layout'], 'type': 'VkImageLayout'},
    }
}
