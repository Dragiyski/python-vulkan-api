import ctypes

class VkPipelineFragmentShadingRateStateCreateInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkGraphicsPipelineCreateInfo',
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
        'fragmentSize': 'fragment_size',
        'combinerOps': 'combiner_ops',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_fragment_shading_rate',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'combinerOps': 'VkFragmentShadingRateCombinerOpKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_STATE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_STATE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkPipelineFragmentShadingRateStateCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentSize', VkExtent2D),
    ('combinerOps', ctypes.ARRAY(ctypes.c_int, 2)),
]

VkPipelineFragmentShadingRateStateCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentSize': VkExtent2D,
    'combinerOps': ctypes.ARRAY(ctypes.c_int, 2),
}
