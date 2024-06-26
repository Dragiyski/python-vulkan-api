import ctypes

class VkPipelineViewportSwizzleStateCreateInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPipelineViewportStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkViewportSwizzleNV',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'viewportCount': 'viewport_count',
        'pViewportSwizzles': 'viewport_swizzles',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_viewport_swizzle',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineViewportSwizzleStateCreateFlagsNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SWIZZLE_STATE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SWIZZLE_STATE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkViewportSwizzleNV import VkViewportSwizzleNV

VkPipelineViewportSwizzleStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportSwizzles', ctypes.POINTER(VkViewportSwizzleNV)),
]

VkPipelineViewportSwizzleStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'viewportCount': ctypes.c_uint32,
    'pViewportSwizzles': ctypes.POINTER(VkViewportSwizzleNV),
}
