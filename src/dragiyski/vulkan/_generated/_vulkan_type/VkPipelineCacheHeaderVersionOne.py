import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('headerSize', ctypes.c_uint32),
        ('headerVersion', ctypes.c_int),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]
