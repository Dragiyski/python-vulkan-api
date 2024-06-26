import ctypes

class VkShaderStatisticsInfoAMD(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkShaderResourceUsageAMD',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'shaderStageMask': 'shader_stage_mask',
        'resourceUsage': 'resource_usage',
        'numPhysicalVgprs': 'num_physical_vgprs',
        'numPhysicalSgprs': 'num_physical_sgprs',
        'numAvailableVgprs': 'num_available_vgprs',
        'numAvailableSgprs': 'num_available_sgprs',
        'computeWorkGroupSize': 'compute_work_group_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMD_shader_info',
    }
    _vk_enum_ = {
        'shaderStageMask': 'VkShaderStageFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkShaderResourceUsageAMD import VkShaderResourceUsageAMD

VkShaderStatisticsInfoAMD._fields_ = [
    ('shaderStageMask', ctypes.c_uint32),
    ('resourceUsage', VkShaderResourceUsageAMD),
    ('numPhysicalVgprs', ctypes.c_uint32),
    ('numPhysicalSgprs', ctypes.c_uint32),
    ('numAvailableVgprs', ctypes.c_uint32),
    ('numAvailableSgprs', ctypes.c_uint32),
    ('computeWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
]

VkShaderStatisticsInfoAMD._type_ = {
    'shaderStageMask': ctypes.c_uint32,
    'resourceUsage': VkShaderResourceUsageAMD,
    'numPhysicalVgprs': ctypes.c_uint32,
    'numPhysicalSgprs': ctypes.c_uint32,
    'numAvailableVgprs': ctypes.c_uint32,
    'numAvailableSgprs': ctypes.c_uint32,
    'computeWorkGroupSize': ctypes.ARRAY(ctypes.c_uint32, 3),
}
