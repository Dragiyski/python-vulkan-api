import ctypes

class VkSubpassDependency2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcSubpass', ctypes.c_uint32),
        ('dstSubpass', ctypes.c_uint32),
        ('srcStageMask', ctypes.c_uint32),
        ('dstStageMask', ctypes.c_uint32),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
        ('dependencyFlags', ctypes.c_uint32),
        ('viewOffset', ctypes.c_int32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkMemoryBarrier2',
    }
    _includes_ = set()
    _included_in_ = {
        'VkRenderPassCreateInfo2',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcSubpass': 'src_subpass',
        'dstSubpass': 'dst_subpass',
        'srcStageMask': 'src_stage_mask',
        'dstStageMask': 'dst_stage_mask',
        'srcAccessMask': 'src_access_mask',
        'dstAccessMask': 'dst_access_mask',
        'dependencyFlags': 'dependency_flags',
        'viewOffset': 'view_offset',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'srcStageMask': 'VkPipelineStageFlags',
        'dstStageMask': 'VkPipelineStageFlags',
        'srcAccessMask': 'VkAccessFlags',
        'dstAccessMask': 'VkAccessFlags',
        'dependencyFlags': 'VkDependencyFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SUBPASS_DEPENDENCY_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_DEPENDENCY_2
        for function in self._init_:
            function(self, *args, **kwargs)

VkSubpassDependency2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcSubpass': ctypes.c_uint32,
    'dstSubpass': ctypes.c_uint32,
    'srcStageMask': ctypes.c_uint32,
    'dstStageMask': ctypes.c_uint32,
    'srcAccessMask': ctypes.c_uint32,
    'dstAccessMask': ctypes.c_uint32,
    'dependencyFlags': ctypes.c_uint32,
    'viewOffset': ctypes.c_int32,
}
