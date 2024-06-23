import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseBufferMemoryBindInfo import CType as VkSparseBufferMemoryBindInfo
from .VkSparseImageMemoryBindInfo import CType as VkSparseImageMemoryBindInfo
from .VkSparseImageOpaqueMemoryBindInfo import CType as VkSparseImageOpaqueMemoryBindInfo

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDeviceGroupBindSparseInfo',
        'VkFrameBoundaryEXT',
        'VkTimelineSemaphoreSubmitInfo',
    },
    'includes': {
        'VkSparseBufferMemoryBindInfo',
        'VkSparseImageMemoryBindInfo',
        'VkSparseImageOpaqueMemoryBindInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkQueueBindSparse',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_SPARSE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'waitSemaphoreCount': {'python_name': ['wait', 'semaphore', 'count']},
        'pWaitSemaphores': {'python_name': ['p', 'wait', 'semaphores'], 'len': [['waitSemaphoreCount']]},
        'bufferBindCount': {'python_name': ['buffer', 'bind', 'count']},
        'pBufferBinds': {'python_name': ['p', 'buffer', 'binds'], 'len': [['bufferBindCount']], 'type': 'VkSparseBufferMemoryBindInfo'},
        'imageOpaqueBindCount': {'python_name': ['image', 'opaque', 'bind', 'count']},
        'pImageOpaqueBinds': {'python_name': ['p', 'image', 'opaque', 'binds'], 'len': [['imageOpaqueBindCount']], 'type': 'VkSparseImageOpaqueMemoryBindInfo'},
        'imageBindCount': {'python_name': ['image', 'bind', 'count']},
        'pImageBinds': {'python_name': ['p', 'image', 'binds'], 'len': [['imageBindCount']], 'type': 'VkSparseImageMemoryBindInfo'},
        'signalSemaphoreCount': {'python_name': ['signal', 'semaphore', 'count']},
        'pSignalSemaphores': {'python_name': ['p', 'signal', 'semaphores'], 'len': [['signalSemaphoreCount']]},
    }
}
