import ctypes

class VkSubmitInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'waitSemaphoreCount': ctypes.c_uint32,
            'pWaitSemaphores': ctypes.POINTER(ctypes.c_void_p),
            'pWaitDstStageMask': ctypes.POINTER(ctypes.c_uint32),
            'commandBufferCount': ctypes.c_uint32,
            'pCommandBuffers': ctypes.POINTER(ctypes.c_void_p),
            'signalSemaphoreCount': ctypes.c_uint32,
            'pSignalSemaphores': ctypes.POINTER(ctypes.c_void_p),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreCount', ctypes.c_uint32),
        ('pWaitSemaphores', ctypes.POINTER(ctypes.c_void_p)),
        ('pWaitDstStageMask', ctypes.POINTER(ctypes.c_uint32)),
        ('commandBufferCount', ctypes.c_uint32),
        ('pCommandBuffers', ctypes.POINTER(ctypes.c_void_p)),
        ('signalSemaphoreCount', ctypes.c_uint32),
        ('pSignalSemaphores', ctypes.POINTER(ctypes.c_void_p)),
    ]
