import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingMotionBlur', ctypes.c_uint32),
        ('rayTracingMotionBlurPipelineTraceRaysIndirect', ctypes.c_uint32),
    ]
