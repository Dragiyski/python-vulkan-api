import ctypes

class VkMemoryBarrier2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcStageMask', ctypes.c_uint64),
        ('srcAccessMask', ctypes.c_uint64),
        ('dstStageMask', ctypes.c_uint64),
        ('dstAccessMask', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = {
        'VkSubpassDependency2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDependencyInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcStageMask': 'src_stage_mask',
        'srcAccessMask': 'src_access_mask',
        'dstStageMask': 'dst_stage_mask',
        'dstAccessMask': 'dst_access_mask',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'srcStageMask': 'VkPipelineStageFlags2',
        'srcAccessMask': 'VkAccessFlags2',
        'dstStageMask': 'VkPipelineStageFlags2',
        'dstAccessMask': 'VkAccessFlags2',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MEMORY_BARRIER_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_BARRIER_2
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryBarrier2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcStageMask': ctypes.c_uint64,
    'srcAccessMask': ctypes.c_uint64,
    'dstStageMask': ctypes.c_uint64,
    'dstAccessMask': ctypes.c_uint64,
}
