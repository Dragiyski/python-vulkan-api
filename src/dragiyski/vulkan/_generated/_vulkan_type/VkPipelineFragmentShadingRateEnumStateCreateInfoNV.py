import ctypes

class VkPipelineFragmentShadingRateEnumStateCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shadingRateType', ctypes.c_int),
        ('shadingRate', ctypes.c_int),
        ('combinerOps', ctypes.ARRAY(ctypes.c_int, 2)),
    ]

    _init_ = []
    _extends_ = {
        'VkGraphicsPipelineCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'shadingRateType': 'shading_rate_type',
        'shadingRate': 'shading_rate',
        'combinerOps': 'combiner_ops',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_fragment_shading_rate_enums',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'shadingRateType': 'VkFragmentShadingRateTypeNV',
        'shadingRate': 'VkFragmentShadingRateNV',
        'combinerOps': 'VkFragmentShadingRateCombinerOpKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_ENUM_STATE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_ENUM_STATE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineFragmentShadingRateEnumStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shadingRateType': ctypes.c_int,
    'shadingRate': ctypes.c_int,
    'combinerOps': ctypes.ARRAY(ctypes.c_int, 2),
}
