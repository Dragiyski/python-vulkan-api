import ctypes, sys

class VkSubmitInfo2(ctypes.Structure):
    pass

sys.modules[__name__] = VkSubmitInfo2

from . import VkCommandBufferSubmitInfo
from . import VkSemaphoreSubmitInfo

VkSubmitInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('waitSemaphoreInfoCount', ctypes.c_uint32),
    ('pWaitSemaphoreInfos', ctypes.POINTER(VkSemaphoreSubmitInfo)),
    ('commandBufferInfoCount', ctypes.c_uint32),
    ('pCommandBufferInfos', ctypes.POINTER(VkCommandBufferSubmitInfo)),
    ('signalSemaphoreInfoCount', ctypes.c_uint32),
    ('pSignalSemaphoreInfos', ctypes.POINTER(VkSemaphoreSubmitInfo)),
]
