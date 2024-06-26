import ctypes

class VkSamplerCreateInfo(ctypes.Structure):
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

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
        'VkSamplerBlockMatchWindowCreateInfoQCOM',
        'VkSamplerBorderColorComponentMappingCreateInfoEXT',
        'VkSamplerCubicWeightsCreateInfoQCOM',
        'VkSamplerCustomBorderColorCreateInfoEXT',
        'VkSamplerReductionModeCreateInfo',
        'VkSamplerYcbcrConversionInfo',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateSampler',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'magFilter': 'mag_filter',
        'minFilter': 'min_filter',
        'mipmapMode': 'mipmap_mode',
        'addressModeU': 'address_mode_u',
        'addressModeV': 'address_mode_v',
        'addressModeW': 'address_mode_w',
        'mipLodBias': 'mip_lod_bias',
        'anisotropyEnable': 'anisotropy_enable',
        'maxAnisotropy': 'max_anisotropy',
        'compareEnable': 'compare_enable',
        'compareOp': 'compare_op',
        'minLod': 'min_lod',
        'maxLod': 'max_lod',
        'borderColor': 'border_color',
        'unnormalizedCoordinates': 'unnormalized_coordinates',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkSamplerCreateFlags',
        'magFilter': 'VkFilter',
        'minFilter': 'VkFilter',
        'mipmapMode': 'VkSamplerMipmapMode',
        'addressModeU': 'VkSamplerAddressMode',
        'addressModeV': 'VkSamplerAddressMode',
        'addressModeW': 'VkSamplerAddressMode',
        'compareOp': 'VkCompareOp',
        'borderColor': 'VkBorderColor',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkSamplerCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'magFilter': ctypes.c_int,
    'minFilter': ctypes.c_int,
    'mipmapMode': ctypes.c_int,
    'addressModeU': ctypes.c_int,
    'addressModeV': ctypes.c_int,
    'addressModeW': ctypes.c_int,
    'mipLodBias': ctypes.c_float,
    'anisotropyEnable': ctypes.c_uint32,
    'maxAnisotropy': ctypes.c_float,
    'compareEnable': ctypes.c_uint32,
    'compareOp': ctypes.c_int,
    'minLod': ctypes.c_float,
    'maxLod': ctypes.c_float,
    'borderColor': ctypes.c_int,
    'unnormalizedCoordinates': ctypes.c_uint32,
}
