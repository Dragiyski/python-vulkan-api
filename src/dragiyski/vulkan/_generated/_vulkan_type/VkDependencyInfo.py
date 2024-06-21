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
