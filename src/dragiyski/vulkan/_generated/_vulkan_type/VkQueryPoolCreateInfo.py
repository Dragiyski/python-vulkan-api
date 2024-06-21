import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('queryType', ctypes.c_int),
        ('queryCount', ctypes.c_uint32),
        ('pipelineStatistics', ctypes.c_uint32),
    ]
