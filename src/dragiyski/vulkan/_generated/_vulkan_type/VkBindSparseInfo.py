import ctypes, sys

class VkBindSparseInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkBindSparseInfo

from . import VkSparseBufferMemoryBindInfo
from . import VkSparseImageMemoryBindInfo
from . import VkSparseImageOpaqueMemoryBindInfo

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
