import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('earlyFragmentMultisampleCoverageAfterSampleCounting', ctypes.c_uint32),
        ('earlyFragmentSampleMaskTestBeforeSampleCounting', ctypes.c_uint32),
        ('depthStencilSwizzleOneSupport', ctypes.c_uint32),
        ('polygonModePointSize', ctypes.c_uint32),
        ('nonStrictSinglePixelWideLinesUseParallelogram', ctypes.c_uint32),
        ('nonStrictWideLinesUseParallelogram', ctypes.c_uint32),
    ]
