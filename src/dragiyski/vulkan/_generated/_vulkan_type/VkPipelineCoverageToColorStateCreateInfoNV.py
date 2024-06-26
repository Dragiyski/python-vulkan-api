import ctypes

class VkPipelineCoverageToColorStateCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('coverageToColorEnable', ctypes.c_uint32),
        ('coverageToColorLocation', ctypes.c_uint32),
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
        'coverageToColorEnable': 'coverage_to_color_enable',
        'coverageToColorLocation': 'coverage_to_color_location',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_fragment_coverage_to_color',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineCoverageToColorStateCreateFlagsNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_TO_COLOR_STATE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_TO_COLOR_STATE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineCoverageToColorStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'coverageToColorEnable': ctypes.c_uint32,
    'coverageToColorLocation': ctypes.c_uint32,
}
