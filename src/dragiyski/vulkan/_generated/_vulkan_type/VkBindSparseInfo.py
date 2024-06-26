import ctypes

class VkBindSparseInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDeviceGroupBindSparseInfo',
        'VkFrameBoundaryEXT',
        'VkTimelineSemaphoreSubmitInfo',
    }
    _includes_ = {
        'VkSparseBufferMemoryBindInfo',
        'VkSparseImageMemoryBindInfo',
        'VkSparseImageOpaqueMemoryBindInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkQueueBindSparse',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'waitSemaphoreCount': 'wait_semaphore_count',
        'pWaitSemaphores': 'wait_semaphores',
        'bufferBindCount': 'buffer_bind_count',
        'pBufferBinds': 'buffer_binds',
        'imageOpaqueBindCount': 'image_opaque_bind_count',
        'pImageOpaqueBinds': 'image_opaque_binds',
        'imageBindCount': 'image_bind_count',
        'pImageBinds': 'image_binds',
        'signalSemaphoreCount': 'signal_semaphore_count',
        'pSignalSemaphores': 'signal_semaphores',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BIND_SPARSE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_SPARSE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSparseBufferMemoryBindInfo import VkSparseBufferMemoryBindInfo
from .VkSparseImageMemoryBindInfo import VkSparseImageMemoryBindInfo
from .VkSparseImageOpaqueMemoryBindInfo import VkSparseImageOpaqueMemoryBindInfo

VkBindSparseInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('waitSemaphoreCount', ctypes.c_uint32),
    ('pWaitSemaphores', ctypes.POINTER(ctypes.c_void_p)),
    ('bufferBindCount', ctypes.c_uint32),
    ('pBufferBinds', ctypes.POINTER(VkSparseBufferMemoryBindInfo)),
    ('imageOpaqueBindCount', ctypes.c_uint32),
    ('pImageOpaqueBinds', ctypes.POINTER(VkSparseImageOpaqueMemoryBindInfo)),
    ('imageBindCount', ctypes.c_uint32),
    ('pImageBinds', ctypes.POINTER(VkSparseImageMemoryBindInfo)),
    ('signalSemaphoreCount', ctypes.c_uint32),
    ('pSignalSemaphores', ctypes.POINTER(ctypes.c_void_p)),
]

VkBindSparseInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'waitSemaphoreCount': ctypes.c_uint32,
    'pWaitSemaphores': ctypes.POINTER(ctypes.c_void_p),
    'bufferBindCount': ctypes.c_uint32,
    'pBufferBinds': ctypes.POINTER(VkSparseBufferMemoryBindInfo),
    'imageOpaqueBindCount': ctypes.c_uint32,
    'pImageOpaqueBinds': ctypes.POINTER(VkSparseImageOpaqueMemoryBindInfo),
    'imageBindCount': ctypes.c_uint32,
    'pImageBinds': ctypes.POINTER(VkSparseImageMemoryBindInfo),
    'signalSemaphoreCount': ctypes.c_uint32,
    'pSignalSemaphores': ctypes.POINTER(ctypes.c_void_p),
}
