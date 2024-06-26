import ctypes

class VkCommandBufferInheritanceViewportScissorInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkCommandBufferInheritanceInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkViewport',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'viewportScissor2D': 'viewport_scissor2_d',
        'viewportDepthCount': 'viewport_depth_count',
        'pViewportDepths': 'viewport_depths',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_inherited_viewport_scissor',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_VIEWPORT_SCISSOR_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_VIEWPORT_SCISSOR_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkViewport import VkViewport

VkCommandBufferInheritanceViewportScissorInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportScissor2D', ctypes.c_uint32),
    ('viewportDepthCount', ctypes.c_uint32),
    ('pViewportDepths', ctypes.POINTER(VkViewport)),
]

VkCommandBufferInheritanceViewportScissorInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'viewportScissor2D': ctypes.c_uint32,
    'viewportDepthCount': ctypes.c_uint32,
    'pViewportDepths': ctypes.POINTER(VkViewport),
}
