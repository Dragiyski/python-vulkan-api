import ctypes

class VkPipelineCoverageModulationStateCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('coverageModulationMode', ctypes.c_int),
        ('coverageModulationTableEnable', ctypes.c_uint32),
        ('coverageModulationTableCount', ctypes.c_uint32),
        ('pCoverageModulationTable', ctypes.POINTER(ctypes.c_float)),
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
        'coverageModulationMode': 'coverage_modulation_mode',
        'coverageModulationTableEnable': 'coverage_modulation_table_enable',
        'coverageModulationTableCount': 'coverage_modulation_table_count',
        'pCoverageModulationTable': 'coverage_modulation_table',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_framebuffer_mixed_samples',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineCoverageModulationStateCreateFlagsNV',
        'coverageModulationMode': 'VkCoverageModulationModeNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_MODULATION_STATE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_MODULATION_STATE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineCoverageModulationStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'coverageModulationMode': ctypes.c_int,
    'coverageModulationTableEnable': ctypes.c_uint32,
    'coverageModulationTableCount': ctypes.c_uint32,
    'pCoverageModulationTable': ctypes.POINTER(ctypes.c_float),
}
