import ctypes

class VkSubmitInfo2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'waitSemaphoreInfoCount': ctypes.c_uint32,
            'pWaitSemaphoreInfos': ctypes.POINTER(VkSemaphoreSubmitInfo),
            'commandBufferInfoCount': ctypes.c_uint32,
            'pCommandBufferInfos': ctypes.POINTER(VkCommandBufferSubmitInfo),
            'signalSemaphoreInfoCount': ctypes.c_uint32,
            'pSignalSemaphoreInfos': ctypes.POINTER(VkSemaphoreSubmitInfo),
        }


from .VkCommandBufferSubmitInfo import VkCommandBufferSubmitInfo
from .VkSemaphoreSubmitInfo import VkSemaphoreSubmitInfo

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
