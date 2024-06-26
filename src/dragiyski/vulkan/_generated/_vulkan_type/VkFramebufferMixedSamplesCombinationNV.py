import ctypes

class VkFramebufferMixedSamplesCombinationNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('coverageReductionMode', ctypes.c_int),
        ('rasterizationSamples', ctypes.c_uint32),
        ('depthStencilSamples', ctypes.c_uint32),
        ('colorSamples', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'coverageReductionMode': 'coverage_reduction_mode',
        'rasterizationSamples': 'rasterization_samples',
        'depthStencilSamples': 'depth_stencil_samples',
        'colorSamples': 'color_samples',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_coverage_reduction_mode',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'coverageReductionMode': 'VkCoverageReductionModeNV',
        'depthStencilSamples': 'VkSampleCountFlags',
        'colorSamples': 'VkSampleCountFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FRAMEBUFFER_MIXED_SAMPLES_COMBINATION_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAMEBUFFER_MIXED_SAMPLES_COMBINATION_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkFramebufferMixedSamplesCombinationNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'coverageReductionMode': ctypes.c_int,
    'rasterizationSamples': ctypes.c_uint32,
    'depthStencilSamples': ctypes.c_uint32,
    'colorSamples': ctypes.c_uint32,
}
