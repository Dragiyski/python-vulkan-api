import ctypes

class VkShaderResourceUsageAMD(ctypes.Structure):
    _fields_ = [
        ('numUsedVgprs', ctypes.c_uint32),
        ('numUsedSgprs', ctypes.c_uint32),
        ('ldsSizePerLocalWorkGroup', ctypes.c_uint32),
        ('ldsUsageSizeInBytes', ctypes.c_size_t),
        ('scratchMemUsageInBytes', ctypes.c_size_t),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkShaderStatisticsInfoAMD',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'numUsedVgprs': 'num_used_vgprs',
        'numUsedSgprs': 'num_used_sgprs',
        'ldsSizePerLocalWorkGroup': 'lds_size_per_local_work_group',
        'ldsUsageSizeInBytes': 'lds_usage_size_in_bytes',
        'scratchMemUsageInBytes': 'scratch_mem_usage_in_bytes',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMD_shader_info',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkShaderResourceUsageAMD._type_ = {
    'numUsedVgprs': ctypes.c_uint32,
    'numUsedSgprs': ctypes.c_uint32,
    'ldsSizePerLocalWorkGroup': ctypes.c_uint32,
    'ldsUsageSizeInBytes': ctypes.c_size_t,
    'scratchMemUsageInBytes': ctypes.c_size_t,
}
