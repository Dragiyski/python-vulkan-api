import ctypes

class VkPhysicalDevicePortabilitySubsetFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('constantAlphaColorBlendFactors', ctypes.c_uint32),
        ('events', ctypes.c_uint32),
        ('imageViewFormatReinterpretation', ctypes.c_uint32),
        ('imageViewFormatSwizzle', ctypes.c_uint32),
        ('imageView2DOn3DImage', ctypes.c_uint32),
        ('multisampleArrayImage', ctypes.c_uint32),
        ('mutableComparisonSamplers', ctypes.c_uint32),
        ('pointPolygons', ctypes.c_uint32),
        ('samplerMipLodBias', ctypes.c_uint32),
        ('separateStencilMaskRef', ctypes.c_uint32),
        ('shaderSampleRateInterpolationFunctions', ctypes.c_uint32),
        ('tessellationIsolines', ctypes.c_uint32),
        ('tessellationPointMode', ctypes.c_uint32),
        ('triangleFans', ctypes.c_uint32),
        ('vertexAttributeAccessBeyondStride', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'constantAlphaColorBlendFactors': 'constant_alpha_color_blend_factors',
        'events': 'events',
        'imageViewFormatReinterpretation': 'image_view_format_reinterpretation',
        'imageViewFormatSwizzle': 'image_view_format_swizzle',
        'imageView2DOn3DImage': 'image_view2_don3_dimage',
        'multisampleArrayImage': 'multisample_array_image',
        'mutableComparisonSamplers': 'mutable_comparison_samplers',
        'pointPolygons': 'point_polygons',
        'samplerMipLodBias': 'sampler_mip_lod_bias',
        'separateStencilMaskRef': 'separate_stencil_mask_ref',
        'shaderSampleRateInterpolationFunctions': 'shader_sample_rate_interpolation_functions',
        'tessellationIsolines': 'tessellation_isolines',
        'tessellationPointMode': 'tessellation_point_mode',
        'triangleFans': 'triangle_fans',
        'vertexAttributeAccessBeyondStride': 'vertex_attribute_access_beyond_stride',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_portability_subset',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_FEATURES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_FEATURES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDevicePortabilitySubsetFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'constantAlphaColorBlendFactors': ctypes.c_uint32,
    'events': ctypes.c_uint32,
    'imageViewFormatReinterpretation': ctypes.c_uint32,
    'imageViewFormatSwizzle': ctypes.c_uint32,
    'imageView2DOn3DImage': ctypes.c_uint32,
    'multisampleArrayImage': ctypes.c_uint32,
    'mutableComparisonSamplers': ctypes.c_uint32,
    'pointPolygons': ctypes.c_uint32,
    'samplerMipLodBias': ctypes.c_uint32,
    'separateStencilMaskRef': ctypes.c_uint32,
    'shaderSampleRateInterpolationFunctions': ctypes.c_uint32,
    'tessellationIsolines': ctypes.c_uint32,
    'tessellationPointMode': ctypes.c_uint32,
    'triangleFans': ctypes.c_uint32,
    'vertexAttributeAccessBeyondStride': ctypes.c_uint32,
}
