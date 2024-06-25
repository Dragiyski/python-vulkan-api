import ctypes

class VkPresentInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'waitSemaphoreCount': ctypes.c_uint32,
            'pWaitSemaphores': ctypes.POINTER(ctypes.c_void_p),
            'swapchainCount': ctypes.c_uint32,
            'pSwapchains': ctypes.POINTER(ctypes.c_void_p),
            'pImageIndices': ctypes.POINTER(ctypes.c_uint32),
            'pResults': ctypes.POINTER(ctypes.c_int),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreCount', ctypes.c_uint32),
        ('pWaitSemaphores', ctypes.POINTER(ctypes.c_void_p)),
        ('swapchainCount', ctypes.c_uint32),
        ('pSwapchains', ctypes.POINTER(ctypes.c_void_p)),
        ('pImageIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('pResults', ctypes.POINTER(ctypes.c_int)),
    ]
