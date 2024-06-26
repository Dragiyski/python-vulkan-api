import ctypes

class VkPerformanceOverrideInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('type', ctypes.c_int),
        ('enable', ctypes.c_uint32),
        ('parameter', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdSetPerformanceOverrideINTEL',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'type': 'type',
        'enable': 'enable',
        'parameter': 'parameter',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_INTEL_performance_query',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'type': 'VkPerformanceOverrideTypeINTEL',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PERFORMANCE_OVERRIDE_INFO_INTEL'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_OVERRIDE_INFO_INTEL
        for function in self._init_:
            function(self, *args, **kwargs)

VkPerformanceOverrideInfoINTEL._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'type': ctypes.c_int,
    'enable': ctypes.c_uint32,
    'parameter': ctypes.c_uint64,
}
