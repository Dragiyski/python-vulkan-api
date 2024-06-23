import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('magFilter', ctypes.c_int),
        ('minFilter', ctypes.c_int),
        ('mipmapMode', ctypes.c_int),
        ('addressModeU', ctypes.c_int),
        ('addressModeV', ctypes.c_int),
        ('addressModeW', ctypes.c_int),
        ('mipLodBias', ctypes.c_float),
        ('anisotropyEnable', ctypes.c_uint32),
        ('maxAnisotropy', ctypes.c_float),
        ('compareEnable', ctypes.c_uint32),
        ('compareOp', ctypes.c_int),
        ('minLod', ctypes.c_float),
        ('maxLod', ctypes.c_float),
        ('borderColor', ctypes.c_int),
        ('unnormalizedCoordinates', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
        'VkSamplerBlockMatchWindowCreateInfoQCOM',
        'VkSamplerBorderColorComponentMappingCreateInfoEXT',
        'VkSamplerCubicWeightsCreateInfoQCOM',
        'VkSamplerCustomBorderColorCreateInfoEXT',
        'VkSamplerReductionModeCreateInfo',
        'VkSamplerYcbcrConversionInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateSampler',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkSamplerCreateFlags'},
        'magFilter': {'python_name': ['mag', 'filter'], 'type': 'VkFilter'},
        'minFilter': {'python_name': ['min', 'filter'], 'type': 'VkFilter'},
        'mipmapMode': {'python_name': ['mipmap', 'mode'], 'type': 'VkSamplerMipmapMode'},
        'addressModeU': {'python_name': ['address', 'mode', 'u'], 'type': 'VkSamplerAddressMode'},
        'addressModeV': {'python_name': ['address', 'mode', 'v'], 'type': 'VkSamplerAddressMode'},
        'addressModeW': {'python_name': ['address', 'mode', 'w'], 'type': 'VkSamplerAddressMode'},
        'mipLodBias': {'python_name': ['mip', 'lod', 'bias']},
        'anisotropyEnable': {'python_name': ['anisotropy', 'enable']},
        'maxAnisotropy': {'python_name': ['max', 'anisotropy']},
        'compareEnable': {'python_name': ['compare', 'enable']},
        'compareOp': {'python_name': ['compare', 'op'], 'type': 'VkCompareOp'},
        'minLod': {'python_name': ['min', 'lod']},
        'maxLod': {'python_name': ['max', 'lod']},
        'borderColor': {'python_name': ['border', 'color'], 'type': 'VkBorderColor'},
        'unnormalizedCoordinates': {'python_name': ['unnormalized', 'coordinates']},
    }
}
