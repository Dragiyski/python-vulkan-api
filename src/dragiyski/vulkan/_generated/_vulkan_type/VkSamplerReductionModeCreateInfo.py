import ctypes

class VkSamplerReductionModeCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('reductionMode', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkSamplerCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'reductionMode': 'reduction_mode',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'reductionMode': 'VkSamplerReductionMode',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SAMPLER_REDUCTION_MODE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_REDUCTION_MODE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkSamplerReductionModeCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'reductionMode': ctypes.c_int,
}
