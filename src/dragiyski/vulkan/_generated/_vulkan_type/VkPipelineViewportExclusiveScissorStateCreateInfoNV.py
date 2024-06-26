import ctypes

class VkPipelineViewportExclusiveScissorStateCreateInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPipelineViewportStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkRect2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'exclusiveScissorCount': 'exclusive_scissor_count',
        'pExclusiveScissors': 'exclusive_scissors',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_scissor_exclusive',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_EXCLUSIVE_SCISSOR_STATE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_EXCLUSIVE_SCISSOR_STATE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D

VkPipelineViewportExclusiveScissorStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('exclusiveScissorCount', ctypes.c_uint32),
    ('pExclusiveScissors', ctypes.POINTER(VkRect2D)),
]

VkPipelineViewportExclusiveScissorStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'exclusiveScissorCount': ctypes.c_uint32,
    'pExclusiveScissors': ctypes.POINTER(VkRect2D),
}
