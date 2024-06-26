import ctypes

class VkShadingRatePaletteNV(ctypes.Structure):
    _fields_ = [
        ('shadingRatePaletteEntryCount', ctypes.c_uint32),
        ('pShadingRatePaletteEntries', ctypes.POINTER(ctypes.c_int)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineViewportShadingRateImageStateCreateInfoNV',
    }
    _input_of_ = {
        'vkCmdSetViewportShadingRatePaletteNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'shadingRatePaletteEntryCount': 'shading_rate_palette_entry_count',
        'pShadingRatePaletteEntries': 'shading_rate_palette_entries',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_shading_rate_image',
    }
    _vk_enum_ = {
        'pShadingRatePaletteEntries': 'VkShadingRatePaletteEntryNV',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkShadingRatePaletteNV._type_ = {
    'shadingRatePaletteEntryCount': ctypes.c_uint32,
    'pShadingRatePaletteEntries': ctypes.POINTER(ctypes.c_int),
}
