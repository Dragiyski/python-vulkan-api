import ctypes

class VkDependencyInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkBufferMemoryBarrier2',
        'VkImageMemoryBarrier2',
        'VkMemoryBarrier2',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdPipelineBarrier2',
        'vkCmdSetEvent2',
        'vkCmdWaitEvents2',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'dependencyFlags': 'dependency_flags',
        'memoryBarrierCount': 'memory_barrier_count',
        'pMemoryBarriers': 'memory_barriers',
        'bufferMemoryBarrierCount': 'buffer_memory_barrier_count',
        'pBufferMemoryBarriers': 'buffer_memory_barriers',
        'imageMemoryBarrierCount': 'image_memory_barrier_count',
        'pImageMemoryBarriers': 'image_memory_barriers',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'dependencyFlags': 'VkDependencyFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEPENDENCY_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEPENDENCY_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkBufferMemoryBarrier2 import VkBufferMemoryBarrier2
from .VkImageMemoryBarrier2 import VkImageMemoryBarrier2
from .VkMemoryBarrier2 import VkMemoryBarrier2

VkDependencyInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('dependencyFlags', ctypes.c_uint32),
    ('memoryBarrierCount', ctypes.c_uint32),
    ('pMemoryBarriers', ctypes.POINTER(VkMemoryBarrier2)),
    ('bufferMemoryBarrierCount', ctypes.c_uint32),
    ('pBufferMemoryBarriers', ctypes.POINTER(VkBufferMemoryBarrier2)),
    ('imageMemoryBarrierCount', ctypes.c_uint32),
    ('pImageMemoryBarriers', ctypes.POINTER(VkImageMemoryBarrier2)),
]

VkDependencyInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'dependencyFlags': ctypes.c_uint32,
    'memoryBarrierCount': ctypes.c_uint32,
    'pMemoryBarriers': ctypes.POINTER(VkMemoryBarrier2),
    'bufferMemoryBarrierCount': ctypes.c_uint32,
    'pBufferMemoryBarriers': ctypes.POINTER(VkBufferMemoryBarrier2),
    'imageMemoryBarrierCount': ctypes.c_uint32,
    'pImageMemoryBarriers': ctypes.POINTER(VkImageMemoryBarrier2),
}
