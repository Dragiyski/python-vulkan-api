import ctypes

class VkPushConstantsInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('layout', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
        ('pValues', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineLayoutCreateInfo',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdPushConstants2KHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'layout': 'layout',
        'stageFlags': 'stage_flags',
        'offset': 'offset',
        'size': 'size',
        'pValues': 'values',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance6',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'stageFlags': 'VkShaderStageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PUSH_CONSTANTS_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PUSH_CONSTANTS_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPushConstantsInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'layout': ctypes.c_void_p,
    'stageFlags': ctypes.c_uint32,
    'offset': ctypes.c_uint32,
    'size': ctypes.c_uint32,
    'pValues': ctypes.c_void_p,
}
