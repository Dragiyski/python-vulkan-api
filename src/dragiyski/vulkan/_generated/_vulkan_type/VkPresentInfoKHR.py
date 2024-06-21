import ctypes

class CType(ctypes.Structure):
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
