import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderGroupHandleSize', ctypes.c_uint32),
        ('maxRayRecursionDepth', ctypes.c_uint32),
        ('maxShaderGroupStride', ctypes.c_uint32),
        ('shaderGroupBaseAlignment', ctypes.c_uint32),
        ('shaderGroupHandleCaptureReplaySize', ctypes.c_uint32),
        ('maxRayDispatchInvocationCount', ctypes.c_uint32),
        ('shaderGroupHandleAlignment', ctypes.c_uint32),
        ('maxRayHitAttributeSize', ctypes.c_uint32),
    ]
