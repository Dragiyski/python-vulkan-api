import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('gopFrameCount', ctypes.c_uint32),
        ('idrPeriod', ctypes.c_uint32),
        ('consecutiveBFrameCount', ctypes.c_uint32),
        ('temporalLayerCount', ctypes.c_uint32),
    ]
