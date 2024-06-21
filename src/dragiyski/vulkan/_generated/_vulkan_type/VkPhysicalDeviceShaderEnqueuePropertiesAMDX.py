import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxExecutionGraphDepth', ctypes.c_uint32),
        ('maxExecutionGraphShaderOutputNodes', ctypes.c_uint32),
        ('maxExecutionGraphShaderPayloadSize', ctypes.c_uint32),
        ('maxExecutionGraphShaderPayloadCount', ctypes.c_uint32),
        ('executionGraphDispatchAddressAlignment', ctypes.c_uint32),
    ]
