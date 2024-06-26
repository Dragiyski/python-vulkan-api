import ctypes

class VkPipelineRasterizationConservativeStateCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('conservativeRasterizationMode', ctypes.c_int),
        ('extraPrimitiveOverestimationSize', ctypes.c_float),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineRasterizationStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'conservativeRasterizationMode': 'conservative_rasterization_mode',
        'extraPrimitiveOverestimationSize': 'extra_primitive_overestimation_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_conservative_rasterization',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineRasterizationConservativeStateCreateFlagsEXT',
        'conservativeRasterizationMode': 'VkConservativeRasterizationModeEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_CONSERVATIVE_STATE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_CONSERVATIVE_STATE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineRasterizationConservativeStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'conservativeRasterizationMode': ctypes.c_int,
    'extraPrimitiveOverestimationSize': ctypes.c_float,
}
