import ctypes

class VkPipelineViewportWScalingStateCreateInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPipelineViewportStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkViewportWScalingNV',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'viewportWScalingEnable': 'viewport_wscaling_enable',
        'viewportCount': 'viewport_count',
        'pViewportWScalings': 'viewport_wscalings',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_clip_space_w_scaling',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_W_SCALING_STATE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_W_SCALING_STATE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkViewportWScalingNV import VkViewportWScalingNV

VkPipelineViewportWScalingStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportWScalingEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportWScalings', ctypes.POINTER(VkViewportWScalingNV)),
]

VkPipelineViewportWScalingStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'viewportWScalingEnable': ctypes.c_uint32,
    'viewportCount': ctypes.c_uint32,
    'pViewportWScalings': ctypes.POINTER(VkViewportWScalingNV),
}
