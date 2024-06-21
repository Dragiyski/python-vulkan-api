import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderTileImageColorReadAccess', ctypes.c_uint32),
        ('shaderTileImageDepthReadAccess', ctypes.c_uint32),
        ('shaderTileImageStencilReadAccess', ctypes.c_uint32),
    ]
