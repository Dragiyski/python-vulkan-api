import ctypes

class VkBufferCollectionPropertiesFUCHSIA(ctypes.Structure):
    _init_ = []
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
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'memoryTypeBits': 'memory_type_bits',
        'bufferCount': 'buffer_count',
        'createInfoIndex': 'create_info_index',
        'sysmemPixelFormat': 'sysmem_pixel_format',
        'formatFeatures': 'format_features',
        'sysmemColorSpaceIndex': 'sysmem_color_space_index',
        'samplerYcbcrConversionComponents': 'sampler_ycbcr_conversion_components',
        'suggestedYcbcrModel': 'suggested_ycbcr_model',
        'suggestedYcbcrRange': 'suggested_ycbcr_range',
        'suggestedXChromaOffset': 'suggested_xchroma_offset',
        'suggestedYChromaOffset': 'suggested_ychroma_offset',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_FUCHSIA_buffer_collection',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'formatFeatures': 'VkFormatFeatureFlags',
        'suggestedYcbcrModel': 'VkSamplerYcbcrModelConversion',
        'suggestedYcbcrRange': 'VkSamplerYcbcrRange',
        'suggestedXChromaOffset': 'VkChromaLocation',
        'suggestedYChromaOffset': 'VkChromaLocation',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BUFFER_COLLECTION_PROPERTIES_FUCHSIA'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_COLLECTION_PROPERTIES_FUCHSIA
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkComponentMapping import VkComponentMapping
from .VkSysmemColorSpaceFUCHSIA import VkSysmemColorSpaceFUCHSIA

VkBufferCollectionPropertiesFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryTypeBits', ctypes.c_uint32),
    ('bufferCount', ctypes.c_uint32),
    ('createInfoIndex', ctypes.c_uint32),
    ('sysmemPixelFormat', ctypes.c_uint64),
    ('formatFeatures', ctypes.c_uint32),
    ('sysmemColorSpaceIndex', VkSysmemColorSpaceFUCHSIA),
    ('samplerYcbcrConversionComponents', VkComponentMapping),
    ('suggestedYcbcrModel', ctypes.c_int),
    ('suggestedYcbcrRange', ctypes.c_int),
    ('suggestedXChromaOffset', ctypes.c_int),
    ('suggestedYChromaOffset', ctypes.c_int),
]

VkBufferCollectionPropertiesFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryTypeBits': ctypes.c_uint32,
    'bufferCount': ctypes.c_uint32,
    'createInfoIndex': ctypes.c_uint32,
    'sysmemPixelFormat': ctypes.c_uint64,
    'formatFeatures': ctypes.c_uint32,
    'sysmemColorSpaceIndex': VkSysmemColorSpaceFUCHSIA,
    'samplerYcbcrConversionComponents': VkComponentMapping,
    'suggestedYcbcrModel': ctypes.c_int,
    'suggestedYcbcrRange': ctypes.c_int,
    'suggestedXChromaOffset': ctypes.c_int,
    'suggestedYChromaOffset': ctypes.c_int,
}
