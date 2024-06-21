import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreValuesCount', ctypes.c_uint32),
        ('pWaitSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
        ('signalSemaphoreValuesCount', ctypes.c_uint32),
        ('pSignalSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
    ]
