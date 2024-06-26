import ctypes

class VkMultisampledRenderToSingleSampledInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multisampledRenderToSingleSampledEnable', ctypes.c_uint32),
        ('rasterizationSamples', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkRenderingInfo',
        'VkSubpassDescription2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'multisampledRenderToSingleSampledEnable': 'multisampled_render_to_single_sampled_enable',
        'rasterizationSamples': 'rasterization_samples',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_multisampled_render_to_single_sampled',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MULTISAMPLED_RENDER_TO_SINGLE_SAMPLED_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MULTISAMPLED_RENDER_TO_SINGLE_SAMPLED_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkMultisampledRenderToSingleSampledInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'multisampledRenderToSingleSampledEnable': ctypes.c_uint32,
    'rasterizationSamples': ctypes.c_uint32,
}
