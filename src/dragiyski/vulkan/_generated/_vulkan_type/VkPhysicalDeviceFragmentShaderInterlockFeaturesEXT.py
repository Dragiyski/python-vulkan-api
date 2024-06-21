import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentShaderSampleInterlock', ctypes.c_uint32),
        ('fragmentShaderPixelInterlock', ctypes.c_uint32),
        ('fragmentShaderShadingRateInterlock', ctypes.c_uint32),
    ]
