import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxWorkGroupCount', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
        ('maxOutputClusterCount', ctypes.c_uint32),
        ('indirectBufferOffsetAlignment', ctypes.c_uint64),
    ]
