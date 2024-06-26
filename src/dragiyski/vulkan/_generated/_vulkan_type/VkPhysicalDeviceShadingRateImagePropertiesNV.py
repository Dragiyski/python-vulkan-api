import ctypes

class VkPhysicalDeviceShadingRateImagePropertiesNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'shadingRateTexelSize': 'shading_rate_texel_size',
        'shadingRatePaletteSize': 'shading_rate_palette_size',
        'shadingRateMaxCoarseSamples': 'shading_rate_max_coarse_samples',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_shading_rate_image',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceShadingRateImagePropertiesNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateTexelSize', VkExtent2D),
    ('shadingRatePaletteSize', ctypes.c_uint32),
    ('shadingRateMaxCoarseSamples', ctypes.c_uint32),
]

VkPhysicalDeviceShadingRateImagePropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shadingRateTexelSize': VkExtent2D,
    'shadingRatePaletteSize': ctypes.c_uint32,
    'shadingRateMaxCoarseSamples': ctypes.c_uint32,
}
