import ctypes

class VkPipelineViewportShadingRateImageStateCreateInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPipelineViewportStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkShadingRatePaletteNV',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'shadingRateImageEnable': 'shading_rate_image_enable',
        'viewportCount': 'viewport_count',
        'pShadingRatePalettes': 'shading_rate_palettes',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_shading_rate_image',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SHADING_RATE_IMAGE_STATE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SHADING_RATE_IMAGE_STATE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkShadingRatePaletteNV import VkShadingRatePaletteNV

VkPipelineViewportShadingRateImageStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateImageEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pShadingRatePalettes', ctypes.POINTER(VkShadingRatePaletteNV)),
]

VkPipelineViewportShadingRateImageStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shadingRateImageEnable': ctypes.c_uint32,
    'viewportCount': ctypes.c_uint32,
    'pShadingRatePalettes': ctypes.POINTER(VkShadingRatePaletteNV),
}
