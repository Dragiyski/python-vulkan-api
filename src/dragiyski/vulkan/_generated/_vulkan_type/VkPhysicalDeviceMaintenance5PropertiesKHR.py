import ctypes

class VkPhysicalDeviceMaintenance5PropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('earlyFragmentMultisampleCoverageAfterSampleCounting', ctypes.c_uint32),
        ('earlyFragmentSampleMaskTestBeforeSampleCounting', ctypes.c_uint32),
        ('depthStencilSwizzleOneSupport', ctypes.c_uint32),
        ('polygonModePointSize', ctypes.c_uint32),
        ('nonStrictSinglePixelWideLinesUseParallelogram', ctypes.c_uint32),
        ('nonStrictWideLinesUseParallelogram', ctypes.c_uint32),
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
        'earlyFragmentMultisampleCoverageAfterSampleCounting': 'early_fragment_multisample_coverage_after_sample_counting',
        'earlyFragmentSampleMaskTestBeforeSampleCounting': 'early_fragment_sample_mask_test_before_sample_counting',
        'depthStencilSwizzleOneSupport': 'depth_stencil_swizzle_one_support',
        'polygonModePointSize': 'polygon_mode_point_size',
        'nonStrictSinglePixelWideLinesUseParallelogram': 'non_strict_single_pixel_wide_lines_use_parallelogram',
        'nonStrictWideLinesUseParallelogram': 'non_strict_wide_lines_use_parallelogram',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance5',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_5_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_5_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceMaintenance5PropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'earlyFragmentMultisampleCoverageAfterSampleCounting': ctypes.c_uint32,
    'earlyFragmentSampleMaskTestBeforeSampleCounting': ctypes.c_uint32,
    'depthStencilSwizzleOneSupport': ctypes.c_uint32,
    'polygonModePointSize': ctypes.c_uint32,
    'nonStrictSinglePixelWideLinesUseParallelogram': ctypes.c_uint32,
    'nonStrictWideLinesUseParallelogram': ctypes.c_uint32,
}
