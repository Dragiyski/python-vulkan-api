import ctypes

class VkBufferMemoryBarrier2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcStageMask', ctypes.c_uint64),
        ('srcAccessMask', ctypes.c_uint64),
        ('dstStageMask', ctypes.c_uint64),
        ('dstAccessMask', ctypes.c_uint64),
        ('srcQueueFamilyIndex', ctypes.c_uint32),
        ('dstQueueFamilyIndex', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkExternalMemoryAcquireUnmodifiedEXT',
    }
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
        'srcQueueFamilyIndex': 'src_queue_family_index',
        'dstQueueFamilyIndex': 'dst_queue_family_index',
        'buffer': 'buffer',
        'offset': 'offset',
        'size': 'size',
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
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER_2
        for function in self._init_:
            function(self, *args, **kwargs)

VkBufferMemoryBarrier2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcStageMask': ctypes.c_uint64,
    'srcAccessMask': ctypes.c_uint64,
    'dstStageMask': ctypes.c_uint64,
    'dstAccessMask': ctypes.c_uint64,
    'srcQueueFamilyIndex': ctypes.c_uint32,
    'dstQueueFamilyIndex': ctypes.c_uint32,
    'buffer': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
