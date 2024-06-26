import ctypes

class VkPhysicalDeviceExtendedDynamicState3FeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('extendedDynamicState3TessellationDomainOrigin', ctypes.c_uint32),
        ('extendedDynamicState3DepthClampEnable', ctypes.c_uint32),
        ('extendedDynamicState3PolygonMode', ctypes.c_uint32),
        ('extendedDynamicState3RasterizationSamples', ctypes.c_uint32),
        ('extendedDynamicState3SampleMask', ctypes.c_uint32),
        ('extendedDynamicState3AlphaToCoverageEnable', ctypes.c_uint32),
        ('extendedDynamicState3AlphaToOneEnable', ctypes.c_uint32),
        ('extendedDynamicState3LogicOpEnable', ctypes.c_uint32),
        ('extendedDynamicState3ColorBlendEnable', ctypes.c_uint32),
        ('extendedDynamicState3ColorBlendEquation', ctypes.c_uint32),
        ('extendedDynamicState3ColorWriteMask', ctypes.c_uint32),
        ('extendedDynamicState3RasterizationStream', ctypes.c_uint32),
        ('extendedDynamicState3ConservativeRasterizationMode', ctypes.c_uint32),
        ('extendedDynamicState3ExtraPrimitiveOverestimationSize', ctypes.c_uint32),
        ('extendedDynamicState3DepthClipEnable', ctypes.c_uint32),
        ('extendedDynamicState3SampleLocationsEnable', ctypes.c_uint32),
        ('extendedDynamicState3ColorBlendAdvanced', ctypes.c_uint32),
        ('extendedDynamicState3ProvokingVertexMode', ctypes.c_uint32),
        ('extendedDynamicState3LineRasterizationMode', ctypes.c_uint32),
        ('extendedDynamicState3LineStippleEnable', ctypes.c_uint32),
        ('extendedDynamicState3DepthClipNegativeOneToOne', ctypes.c_uint32),
        ('extendedDynamicState3ViewportWScalingEnable', ctypes.c_uint32),
        ('extendedDynamicState3ViewportSwizzle', ctypes.c_uint32),
        ('extendedDynamicState3CoverageToColorEnable', ctypes.c_uint32),
        ('extendedDynamicState3CoverageToColorLocation', ctypes.c_uint32),
        ('extendedDynamicState3CoverageModulationMode', ctypes.c_uint32),
        ('extendedDynamicState3CoverageModulationTableEnable', ctypes.c_uint32),
        ('extendedDynamicState3CoverageModulationTable', ctypes.c_uint32),
        ('extendedDynamicState3CoverageReductionMode', ctypes.c_uint32),
        ('extendedDynamicState3RepresentativeFragmentTestEnable', ctypes.c_uint32),
        ('extendedDynamicState3ShadingRateImageEnable', ctypes.c_uint32),
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
        'extendedDynamicState3TessellationDomainOrigin': 'extended_dynamic_state3_tessellation_domain_origin',
        'extendedDynamicState3DepthClampEnable': 'extended_dynamic_state3_depth_clamp_enable',
        'extendedDynamicState3PolygonMode': 'extended_dynamic_state3_polygon_mode',
        'extendedDynamicState3RasterizationSamples': 'extended_dynamic_state3_rasterization_samples',
        'extendedDynamicState3SampleMask': 'extended_dynamic_state3_sample_mask',
        'extendedDynamicState3AlphaToCoverageEnable': 'extended_dynamic_state3_alpha_to_coverage_enable',
        'extendedDynamicState3AlphaToOneEnable': 'extended_dynamic_state3_alpha_to_one_enable',
        'extendedDynamicState3LogicOpEnable': 'extended_dynamic_state3_logic_op_enable',
        'extendedDynamicState3ColorBlendEnable': 'extended_dynamic_state3_color_blend_enable',
        'extendedDynamicState3ColorBlendEquation': 'extended_dynamic_state3_color_blend_equation',
        'extendedDynamicState3ColorWriteMask': 'extended_dynamic_state3_color_write_mask',
        'extendedDynamicState3RasterizationStream': 'extended_dynamic_state3_rasterization_stream',
        'extendedDynamicState3ConservativeRasterizationMode': 'extended_dynamic_state3_conservative_rasterization_mode',
        'extendedDynamicState3ExtraPrimitiveOverestimationSize': 'extended_dynamic_state3_extra_primitive_overestimation_size',
        'extendedDynamicState3DepthClipEnable': 'extended_dynamic_state3_depth_clip_enable',
        'extendedDynamicState3SampleLocationsEnable': 'extended_dynamic_state3_sample_locations_enable',
        'extendedDynamicState3ColorBlendAdvanced': 'extended_dynamic_state3_color_blend_advanced',
        'extendedDynamicState3ProvokingVertexMode': 'extended_dynamic_state3_provoking_vertex_mode',
        'extendedDynamicState3LineRasterizationMode': 'extended_dynamic_state3_line_rasterization_mode',
        'extendedDynamicState3LineStippleEnable': 'extended_dynamic_state3_line_stipple_enable',
        'extendedDynamicState3DepthClipNegativeOneToOne': 'extended_dynamic_state3_depth_clip_negative_one_to_one',
        'extendedDynamicState3ViewportWScalingEnable': 'extended_dynamic_state3_viewport_wscaling_enable',
        'extendedDynamicState3ViewportSwizzle': 'extended_dynamic_state3_viewport_swizzle',
        'extendedDynamicState3CoverageToColorEnable': 'extended_dynamic_state3_coverage_to_color_enable',
        'extendedDynamicState3CoverageToColorLocation': 'extended_dynamic_state3_coverage_to_color_location',
        'extendedDynamicState3CoverageModulationMode': 'extended_dynamic_state3_coverage_modulation_mode',
        'extendedDynamicState3CoverageModulationTableEnable': 'extended_dynamic_state3_coverage_modulation_table_enable',
        'extendedDynamicState3CoverageModulationTable': 'extended_dynamic_state3_coverage_modulation_table',
        'extendedDynamicState3CoverageReductionMode': 'extended_dynamic_state3_coverage_reduction_mode',
        'extendedDynamicState3RepresentativeFragmentTestEnable': 'extended_dynamic_state3_representative_fragment_test_enable',
        'extendedDynamicState3ShadingRateImageEnable': 'extended_dynamic_state3_shading_rate_image_enable',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_extended_dynamic_state3',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_3_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_3_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceExtendedDynamicState3FeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'extendedDynamicState3TessellationDomainOrigin': ctypes.c_uint32,
    'extendedDynamicState3DepthClampEnable': ctypes.c_uint32,
    'extendedDynamicState3PolygonMode': ctypes.c_uint32,
    'extendedDynamicState3RasterizationSamples': ctypes.c_uint32,
    'extendedDynamicState3SampleMask': ctypes.c_uint32,
    'extendedDynamicState3AlphaToCoverageEnable': ctypes.c_uint32,
    'extendedDynamicState3AlphaToOneEnable': ctypes.c_uint32,
    'extendedDynamicState3LogicOpEnable': ctypes.c_uint32,
    'extendedDynamicState3ColorBlendEnable': ctypes.c_uint32,
    'extendedDynamicState3ColorBlendEquation': ctypes.c_uint32,
    'extendedDynamicState3ColorWriteMask': ctypes.c_uint32,
    'extendedDynamicState3RasterizationStream': ctypes.c_uint32,
    'extendedDynamicState3ConservativeRasterizationMode': ctypes.c_uint32,
    'extendedDynamicState3ExtraPrimitiveOverestimationSize': ctypes.c_uint32,
    'extendedDynamicState3DepthClipEnable': ctypes.c_uint32,
    'extendedDynamicState3SampleLocationsEnable': ctypes.c_uint32,
    'extendedDynamicState3ColorBlendAdvanced': ctypes.c_uint32,
    'extendedDynamicState3ProvokingVertexMode': ctypes.c_uint32,
    'extendedDynamicState3LineRasterizationMode': ctypes.c_uint32,
    'extendedDynamicState3LineStippleEnable': ctypes.c_uint32,
    'extendedDynamicState3DepthClipNegativeOneToOne': ctypes.c_uint32,
    'extendedDynamicState3ViewportWScalingEnable': ctypes.c_uint32,
    'extendedDynamicState3ViewportSwizzle': ctypes.c_uint32,
    'extendedDynamicState3CoverageToColorEnable': ctypes.c_uint32,
    'extendedDynamicState3CoverageToColorLocation': ctypes.c_uint32,
    'extendedDynamicState3CoverageModulationMode': ctypes.c_uint32,
    'extendedDynamicState3CoverageModulationTableEnable': ctypes.c_uint32,
    'extendedDynamicState3CoverageModulationTable': ctypes.c_uint32,
    'extendedDynamicState3CoverageReductionMode': ctypes.c_uint32,
    'extendedDynamicState3RepresentativeFragmentTestEnable': ctypes.c_uint32,
    'extendedDynamicState3ShadingRateImageEnable': ctypes.c_uint32,
}
