import ctypes

class VkAndroidHardwareBufferFormatProperties2ANDROID(ctypes.Structure):
    _init_ = []
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
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'format': 'format',
        'externalFormat': 'external_format',
        'formatFeatures': 'format_features',
        'samplerYcbcrConversionComponents': 'sampler_ycbcr_conversion_components',
        'suggestedYcbcrModel': 'suggested_ycbcr_model',
        'suggestedYcbcrRange': 'suggested_ycbcr_range',
        'suggestedXChromaOffset': 'suggested_xchroma_offset',
        'suggestedYChromaOffset': 'suggested_ychroma_offset',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ANDROID_external_memory_android_hardware_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'format': 'VkFormat',
        'formatFeatures': 'VkFormatFeatureFlags2',
        'suggestedYcbcrModel': 'VkSamplerYcbcrModelConversion',
        'suggestedYcbcrRange': 'VkSamplerYcbcrRange',
        'suggestedXChromaOffset': 'VkChromaLocation',
        'suggestedYChromaOffset': 'VkChromaLocation',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_PROPERTIES_2_ANDROID'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_PROPERTIES_2_ANDROID
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkComponentMapping import VkComponentMapping

VkAndroidHardwareBufferFormatProperties2ANDROID._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('externalFormat', ctypes.c_uint64),
    ('formatFeatures', ctypes.c_uint64),
    ('samplerYcbcrConversionComponents', VkComponentMapping),
    ('suggestedYcbcrModel', ctypes.c_int),
    ('suggestedYcbcrRange', ctypes.c_int),
    ('suggestedXChromaOffset', ctypes.c_int),
    ('suggestedYChromaOffset', ctypes.c_int),
]

VkAndroidHardwareBufferFormatProperties2ANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'format': ctypes.c_int,
    'externalFormat': ctypes.c_uint64,
    'formatFeatures': ctypes.c_uint64,
    'samplerYcbcrConversionComponents': VkComponentMapping,
    'suggestedYcbcrModel': ctypes.c_int,
    'suggestedYcbcrRange': ctypes.c_int,
    'suggestedXChromaOffset': ctypes.c_int,
    'suggestedYChromaOffset': ctypes.c_int,
}
