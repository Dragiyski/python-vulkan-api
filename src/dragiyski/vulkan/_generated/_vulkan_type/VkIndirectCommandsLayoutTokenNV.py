import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('tokenType', ctypes.c_int),
        ('stream', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('vertexBindingUnit', ctypes.c_uint32),
        ('vertexDynamicStride', ctypes.c_uint32),
        ('pushconstantPipelineLayout', ctypes.c_void_p),
        ('pushconstantShaderStageFlags', ctypes.c_uint32),
        ('pushconstantOffset', ctypes.c_uint32),
        ('pushconstantSize', ctypes.c_uint32),
        ('indirectStateFlags', ctypes.c_uint32),
        ('indexTypeCount', ctypes.c_uint32),
        ('pIndexTypes', ctypes.POINTER(ctypes.c_int)),
        ('pIndexTypeValues', ctypes.POINTER(ctypes.c_uint32)),
    ]
