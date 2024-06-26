import ctypes

class VkComponentMapping(ctypes.Structure):
    _fields_ = [
        ('r', ctypes.c_int),
        ('g', ctypes.c_int),
        ('b', ctypes.c_int),
        ('a', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkAndroidHardwareBufferFormatProperties2ANDROID',
        'VkAndroidHardwareBufferFormatPropertiesANDROID',
        'VkBufferCollectionPropertiesFUCHSIA',
        'VkImageViewCreateInfo',
        'VkSamplerBorderColorComponentMappingCreateInfoEXT',
        'VkSamplerYcbcrConversionCreateInfo',
        'VkScreenBufferFormatPropertiesQNX',
        'VkVideoFormatPropertiesKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'r': 'r',
        'g': 'g',
        'b': 'b',
        'a': 'a',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'r': 'VkComponentSwizzle',
        'g': 'VkComponentSwizzle',
        'b': 'VkComponentSwizzle',
        'a': 'VkComponentSwizzle',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkComponentMapping._type_ = {
    'r': ctypes.c_int,
    'g': ctypes.c_int,
    'b': ctypes.c_int,
    'a': ctypes.c_int,
}
