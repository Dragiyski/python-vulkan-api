import ctypes

class VkBufferMemoryBarrier(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
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
    _included_in_ = set()
    _input_of_ = {
        'vkCmdPipelineBarrier',
        'vkCmdWaitEvents',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'srcAccessMask': 'src_access_mask',
        'dstAccessMask': 'dst_access_mask',
        'srcQueueFamilyIndex': 'src_queue_family_index',
        'dstQueueFamilyIndex': 'dst_queue_family_index',
        'buffer': 'buffer',
        'offset': 'offset',
        'size': 'size',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'srcAccessMask': 'VkAccessFlags',
        'dstAccessMask': 'VkAccessFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER
        for function in self._init_:
            function(self, *args, **kwargs)

VkBufferMemoryBarrier._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcAccessMask': ctypes.c_uint32,
    'dstAccessMask': ctypes.c_uint32,
    'srcQueueFamilyIndex': ctypes.c_uint32,
    'dstQueueFamilyIndex': ctypes.c_uint32,
    'buffer': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
