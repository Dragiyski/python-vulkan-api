import ctypes

class VkPhysicalDeviceFragmentShadingRatePropertiesKHR(ctypes.Structure):
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
        'minFragmentShadingRateAttachmentTexelSize': 'min_fragment_shading_rate_attachment_texel_size',
        'maxFragmentShadingRateAttachmentTexelSize': 'max_fragment_shading_rate_attachment_texel_size',
        'maxFragmentShadingRateAttachmentTexelSizeAspectRatio': 'max_fragment_shading_rate_attachment_texel_size_aspect_ratio',
        'primitiveFragmentShadingRateWithMultipleViewports': 'primitive_fragment_shading_rate_with_multiple_viewports',
        'layeredShadingRateAttachments': 'layered_shading_rate_attachments',
        'fragmentShadingRateNonTrivialCombinerOps': 'fragment_shading_rate_non_trivial_combiner_ops',
        'maxFragmentSize': 'max_fragment_size',
        'maxFragmentSizeAspectRatio': 'max_fragment_size_aspect_ratio',
        'maxFragmentShadingRateCoverageSamples': 'max_fragment_shading_rate_coverage_samples',
        'maxFragmentShadingRateRasterizationSamples': 'max_fragment_shading_rate_rasterization_samples',
        'fragmentShadingRateWithShaderDepthStencilWrites': 'fragment_shading_rate_with_shader_depth_stencil_writes',
        'fragmentShadingRateWithSampleMask': 'fragment_shading_rate_with_sample_mask',
        'fragmentShadingRateWithShaderSampleMask': 'fragment_shading_rate_with_shader_sample_mask',
        'fragmentShadingRateWithConservativeRasterization': 'fragment_shading_rate_with_conservative_rasterization',
        'fragmentShadingRateWithFragmentShaderInterlock': 'fragment_shading_rate_with_fragment_shader_interlock',
        'fragmentShadingRateWithCustomSampleLocations': 'fragment_shading_rate_with_custom_sample_locations',
        'fragmentShadingRateStrictMultiplyCombiner': 'fragment_shading_rate_strict_multiply_combiner',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_fragment_shading_rate',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceFragmentShadingRatePropertiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('minFragmentShadingRateAttachmentTexelSize', VkExtent2D),
    ('maxFragmentShadingRateAttachmentTexelSize', VkExtent2D),
    ('maxFragmentShadingRateAttachmentTexelSizeAspectRatio', ctypes.c_uint32),
    ('primitiveFragmentShadingRateWithMultipleViewports', ctypes.c_uint32),
    ('layeredShadingRateAttachments', ctypes.c_uint32),
    ('fragmentShadingRateNonTrivialCombinerOps', ctypes.c_uint32),
    ('maxFragmentSize', VkExtent2D),
    ('maxFragmentSizeAspectRatio', ctypes.c_uint32),
    ('maxFragmentShadingRateCoverageSamples', ctypes.c_uint32),
    ('maxFragmentShadingRateRasterizationSamples', ctypes.c_uint32),
    ('fragmentShadingRateWithShaderDepthStencilWrites', ctypes.c_uint32),
    ('fragmentShadingRateWithSampleMask', ctypes.c_uint32),
    ('fragmentShadingRateWithShaderSampleMask', ctypes.c_uint32),
    ('fragmentShadingRateWithConservativeRasterization', ctypes.c_uint32),
    ('fragmentShadingRateWithFragmentShaderInterlock', ctypes.c_uint32),
    ('fragmentShadingRateWithCustomSampleLocations', ctypes.c_uint32),
    ('fragmentShadingRateStrictMultiplyCombiner', ctypes.c_uint32),
]

VkPhysicalDeviceFragmentShadingRatePropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'minFragmentShadingRateAttachmentTexelSize': VkExtent2D,
    'maxFragmentShadingRateAttachmentTexelSize': VkExtent2D,
    'maxFragmentShadingRateAttachmentTexelSizeAspectRatio': ctypes.c_uint32,
    'primitiveFragmentShadingRateWithMultipleViewports': ctypes.c_uint32,
    'layeredShadingRateAttachments': ctypes.c_uint32,
    'fragmentShadingRateNonTrivialCombinerOps': ctypes.c_uint32,
    'maxFragmentSize': VkExtent2D,
    'maxFragmentSizeAspectRatio': ctypes.c_uint32,
    'maxFragmentShadingRateCoverageSamples': ctypes.c_uint32,
    'maxFragmentShadingRateRasterizationSamples': ctypes.c_uint32,
    'fragmentShadingRateWithShaderDepthStencilWrites': ctypes.c_uint32,
    'fragmentShadingRateWithSampleMask': ctypes.c_uint32,
    'fragmentShadingRateWithShaderSampleMask': ctypes.c_uint32,
    'fragmentShadingRateWithConservativeRasterization': ctypes.c_uint32,
    'fragmentShadingRateWithFragmentShaderInterlock': ctypes.c_uint32,
    'fragmentShadingRateWithCustomSampleLocations': ctypes.c_uint32,
    'fragmentShadingRateStrictMultiplyCombiner': ctypes.c_uint32,
}
