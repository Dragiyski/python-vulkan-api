import ctypes

class VkPipelineMultisampleStateCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('rasterizationSamples', ctypes.c_uint32),
        ('sampleShadingEnable', ctypes.c_uint32),
        ('minSampleShading', ctypes.c_float),
        ('pSampleMask', ctypes.POINTER(ctypes.c_uint32)),
        ('alphaToCoverageEnable', ctypes.c_uint32),
        ('alphaToOneEnable', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineCoverageModulationStateCreateInfoNV',
        'VkPipelineCoverageReductionStateCreateInfoNV',
        'VkPipelineCoverageToColorStateCreateInfoNV',
        'VkPipelineSampleLocationsStateCreateInfoEXT',
    }
    _includes_ = set()
    _included_in_ = {
        'VkGraphicsPipelineCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'rasterizationSamples': 'rasterization_samples',
        'sampleShadingEnable': 'sample_shading_enable',
        'minSampleShading': 'min_sample_shading',
        'pSampleMask': 'sample_mask',
        'alphaToCoverageEnable': 'alpha_to_coverage_enable',
        'alphaToOneEnable': 'alpha_to_one_enable',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineMultisampleStateCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineMultisampleStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'rasterizationSamples': ctypes.c_uint32,
    'sampleShadingEnable': ctypes.c_uint32,
    'minSampleShading': ctypes.c_float,
    'pSampleMask': ctypes.POINTER(ctypes.c_uint32),
    'alphaToCoverageEnable': ctypes.c_uint32,
    'alphaToOneEnable': ctypes.c_uint32,
}
