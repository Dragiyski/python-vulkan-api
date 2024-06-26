import ctypes

class VkSubpassDependency(ctypes.Structure):
    _fields_ = [
        ('srcSubpass', ctypes.c_uint32),
        ('dstSubpass', ctypes.c_uint32),
        ('srcStageMask', ctypes.c_uint32),
        ('dstStageMask', ctypes.c_uint32),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
        ('dependencyFlags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkRenderPassCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'srcSubpass': 'src_subpass',
        'dstSubpass': 'dst_subpass',
        'srcStageMask': 'src_stage_mask',
        'dstStageMask': 'dst_stage_mask',
        'srcAccessMask': 'src_access_mask',
        'dstAccessMask': 'dst_access_mask',
        'dependencyFlags': 'dependency_flags',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'srcStageMask': 'VkPipelineStageFlags',
        'dstStageMask': 'VkPipelineStageFlags',
        'srcAccessMask': 'VkAccessFlags',
        'dstAccessMask': 'VkAccessFlags',
        'dependencyFlags': 'VkDependencyFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkSubpassDependency._type_ = {
    'srcSubpass': ctypes.c_uint32,
    'dstSubpass': ctypes.c_uint32,
    'srcStageMask': ctypes.c_uint32,
    'dstStageMask': ctypes.c_uint32,
    'srcAccessMask': ctypes.c_uint32,
    'dstAccessMask': ctypes.c_uint32,
    'dependencyFlags': ctypes.c_uint32,
}
