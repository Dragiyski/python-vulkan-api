import ctypes

class VkPipelineViewportStateCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineViewportCoarseSampleOrderStateCreateInfoNV',
        'VkPipelineViewportDepthClipControlCreateInfoEXT',
        'VkPipelineViewportExclusiveScissorStateCreateInfoNV',
        'VkPipelineViewportShadingRateImageStateCreateInfoNV',
        'VkPipelineViewportSwizzleStateCreateInfoNV',
        'VkPipelineViewportWScalingStateCreateInfoNV',
    }
    _includes_ = {
        'VkRect2D',
        'VkViewport',
    }
    _included_in_ = {
        'VkGraphicsPipelineCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'viewportCount': 'viewport_count',
        'pViewports': 'viewports',
        'scissorCount': 'scissor_count',
        'pScissors': 'scissors',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineViewportStateCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D
from .VkViewport import VkViewport

VkPipelineViewportStateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewports', ctypes.POINTER(VkViewport)),
    ('scissorCount', ctypes.c_uint32),
    ('pScissors', ctypes.POINTER(VkRect2D)),
]

VkPipelineViewportStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'viewportCount': ctypes.c_uint32,
    'pViewports': ctypes.POINTER(VkViewport),
    'scissorCount': ctypes.c_uint32,
    'pScissors': ctypes.POINTER(VkRect2D),
}
