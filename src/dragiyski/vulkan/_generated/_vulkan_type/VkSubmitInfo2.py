import ctypes

class CType(ctypes.Structure):
    pass

from .VkCommandBufferSubmitInfo import CType as VkCommandBufferSubmitInfo
from .VkSemaphoreSubmitInfo import CType as VkSemaphoreSubmitInfo

CType._fields_ = [
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
