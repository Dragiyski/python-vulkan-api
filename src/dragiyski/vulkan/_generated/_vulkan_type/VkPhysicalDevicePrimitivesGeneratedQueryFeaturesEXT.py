import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitivesGeneratedQuery', ctypes.c_uint32),
        ('primitivesGeneratedQueryWithRasterizerDiscard', ctypes.c_uint32),
        ('primitivesGeneratedQueryWithNonZeroStreams', ctypes.c_uint32),
    ]
