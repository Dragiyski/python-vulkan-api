import ctypes, sys

class VkDependencyInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkDependencyInfo

from . import VkBufferMemoryBarrier2
from . import VkImageMemoryBarrier2
from . import VkMemoryBarrier2

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
