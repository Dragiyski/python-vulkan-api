import ctypes

class VkPipelineCoverageReductionStateCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('coverageReductionMode', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineMultisampleStateCreateInfo',
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
        'coverageReductionMode': 'coverage_reduction_mode',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_coverage_reduction_mode',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineCoverageReductionStateCreateFlagsNV',
        'coverageReductionMode': 'VkCoverageReductionModeNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_REDUCTION_STATE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_REDUCTION_STATE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineCoverageReductionStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'coverageReductionMode': ctypes.c_int,
}
