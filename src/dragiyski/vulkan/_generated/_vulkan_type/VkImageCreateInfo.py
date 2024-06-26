import ctypes

class VkImageCreateInfo(ctypes.Structure):
    _init_ = []
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
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'imageType': 'image_type',
        'format': 'format',
        'extent': 'extent',
        'mipLevels': 'mip_levels',
        'arrayLayers': 'array_layers',
        'samples': 'samples',
        'tiling': 'tiling',
        'usage': 'usage',
        'sharingMode': 'sharing_mode',
        'queueFamilyIndexCount': 'queue_family_index_count',
        'pQueueFamilyIndices': 'queue_family_indices',
        'initialLayout': 'initial_layout',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkImageCreateFlags',
        'imageType': 'VkImageType',
        'format': 'VkFormat',
        'tiling': 'VkImageTiling',
        'usage': 'VkImageUsageFlags',
        'sharingMode': 'VkSharingMode',
        'initialLayout': 'VkImageLayout',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent3D import VkExtent3D

VkImageCreateInfo._fields_ = [
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

VkImageCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'imageType': ctypes.c_int,
    'format': ctypes.c_int,
    'extent': VkExtent3D,
    'mipLevels': ctypes.c_uint32,
    'arrayLayers': ctypes.c_uint32,
    'samples': ctypes.c_uint32,
    'tiling': ctypes.c_int,
    'usage': ctypes.c_uint32,
    'sharingMode': ctypes.c_int,
    'queueFamilyIndexCount': ctypes.c_uint32,
    'pQueueFamilyIndices': ctypes.POINTER(ctypes.c_uint32),
    'initialLayout': ctypes.c_int,
}
