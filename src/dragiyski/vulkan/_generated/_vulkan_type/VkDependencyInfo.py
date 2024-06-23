import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferMemoryBarrier2 import CType as VkBufferMemoryBarrier2
from .VkImageMemoryBarrier2 import CType as VkImageMemoryBarrier2
from .VkMemoryBarrier2 import CType as VkMemoryBarrier2

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkBufferMemoryBarrier2',
        'VkImageMemoryBarrier2',
        'VkMemoryBarrier2',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdPipelineBarrier2',
        'vkCmdSetEvent2',
        'vkCmdWaitEvents2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEPENDENCY_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'dependencyFlags': {'python_name': ['dependency', 'flags'], 'type': 'VkDependencyFlags'},
        'memoryBarrierCount': {'python_name': ['memory', 'barrier', 'count']},
        'pMemoryBarriers': {'python_name': ['p', 'memory', 'barriers'], 'len': [['memoryBarrierCount']], 'type': 'VkMemoryBarrier2'},
        'bufferMemoryBarrierCount': {'python_name': ['buffer', 'memory', 'barrier', 'count']},
        'pBufferMemoryBarriers': {'python_name': ['p', 'buffer', 'memory', 'barriers'], 'len': [['bufferMemoryBarrierCount']], 'type': 'VkBufferMemoryBarrier2'},
        'imageMemoryBarrierCount': {'python_name': ['image', 'memory', 'barrier', 'count']},
        'pImageMemoryBarriers': {'python_name': ['p', 'image', 'memory', 'barriers'], 'len': [['imageMemoryBarrierCount']], 'type': 'VkImageMemoryBarrier2'},
    }
}
