import ctypes, sys

class VkSubmitInfo(ctypes.Structure):
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

sys.modules[__name__] = VkSubmitInfo
