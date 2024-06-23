import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('r', ctypes.c_int),
        ('g', ctypes.c_int),
        ('b', ctypes.c_int),
        ('a', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkAndroidHardwareBufferFormatProperties2ANDROID',
        'VkAndroidHardwareBufferFormatPropertiesANDROID',
        'VkBufferCollectionPropertiesFUCHSIA',
        'VkImageViewCreateInfo',
        'VkSamplerBorderColorComponentMappingCreateInfoEXT',
        'VkSamplerYcbcrConversionCreateInfo',
        'VkScreenBufferFormatPropertiesQNX',
        'VkVideoFormatPropertiesKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'r': {'python_name': ['r'], 'type': 'VkComponentSwizzle'},
        'g': {'python_name': ['g'], 'type': 'VkComponentSwizzle'},
        'b': {'python_name': ['b'], 'type': 'VkComponentSwizzle'},
        'a': {'python_name': ['a'], 'type': 'VkComponentSwizzle'},
    }
}
