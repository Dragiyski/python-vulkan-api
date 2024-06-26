import ctypes

class VkPhysicalDeviceConservativeRasterizationPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitiveOverestimationSize', ctypes.c_float),
        ('maxExtraPrimitiveOverestimationSize', ctypes.c_float),
        ('extraPrimitiveOverestimationSizeGranularity', ctypes.c_float),
        ('primitiveUnderestimation', ctypes.c_uint32),
        ('conservativePointAndLineRasterization', ctypes.c_uint32),
        ('degenerateTrianglesRasterized', ctypes.c_uint32),
        ('degenerateLinesRasterized', ctypes.c_uint32),
        ('fullyCoveredFragmentShaderInputVariable', ctypes.c_uint32),
        ('conservativeRasterizationPostDepthCoverage', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'primitiveOverestimationSize': 'primitive_overestimation_size',
        'maxExtraPrimitiveOverestimationSize': 'max_extra_primitive_overestimation_size',
        'extraPrimitiveOverestimationSizeGranularity': 'extra_primitive_overestimation_size_granularity',
        'primitiveUnderestimation': 'primitive_underestimation',
        'conservativePointAndLineRasterization': 'conservative_point_and_line_rasterization',
        'degenerateTrianglesRasterized': 'degenerate_triangles_rasterized',
        'degenerateLinesRasterized': 'degenerate_lines_rasterized',
        'fullyCoveredFragmentShaderInputVariable': 'fully_covered_fragment_shader_input_variable',
        'conservativeRasterizationPostDepthCoverage': 'conservative_rasterization_post_depth_coverage',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_conservative_rasterization',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONSERVATIVE_RASTERIZATION_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONSERVATIVE_RASTERIZATION_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceConservativeRasterizationPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'primitiveOverestimationSize': ctypes.c_float,
    'maxExtraPrimitiveOverestimationSize': ctypes.c_float,
    'extraPrimitiveOverestimationSizeGranularity': ctypes.c_float,
    'primitiveUnderestimation': ctypes.c_uint32,
    'conservativePointAndLineRasterization': ctypes.c_uint32,
    'degenerateTrianglesRasterized': ctypes.c_uint32,
    'degenerateLinesRasterized': ctypes.c_uint32,
    'fullyCoveredFragmentShaderInputVariable': ctypes.c_uint32,
    'conservativeRasterizationPostDepthCoverage': ctypes.c_uint32,
}
