import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedDepthResolveModes', ctypes.c_uint32),
        ('supportedStencilResolveModes', ctypes.c_uint32),
        ('independentResolveNone', ctypes.c_uint32),
        ('independentResolve', ctypes.c_uint32),
    ]
