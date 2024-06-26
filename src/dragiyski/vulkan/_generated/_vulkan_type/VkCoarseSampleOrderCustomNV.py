import ctypes

class VkCoarseSampleOrderCustomNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkCoarseSampleLocationNV',
    }
    _included_in_ = {
        'VkPipelineViewportCoarseSampleOrderStateCreateInfoNV',
    }
    _input_of_ = {
        'vkCmdSetCoarseSampleOrderNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'shadingRate': 'shading_rate',
        'sampleCount': 'sample_count',
        'sampleLocationCount': 'sample_location_count',
        'pSampleLocations': 'sample_locations',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_shading_rate_image',
    }
    _vk_enum_ = {
        'shadingRate': 'VkShadingRatePaletteEntryNV',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkCoarseSampleLocationNV import VkCoarseSampleLocationNV

VkCoarseSampleOrderCustomNV._fields_ = [
    ('shadingRate', ctypes.c_int),
    ('sampleCount', ctypes.c_uint32),
    ('sampleLocationCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkCoarseSampleLocationNV)),
]

VkCoarseSampleOrderCustomNV._type_ = {
    'shadingRate': ctypes.c_int,
    'sampleCount': ctypes.c_uint32,
    'sampleLocationCount': ctypes.c_uint32,
    'pSampleLocations': ctypes.POINTER(VkCoarseSampleLocationNV),
}
