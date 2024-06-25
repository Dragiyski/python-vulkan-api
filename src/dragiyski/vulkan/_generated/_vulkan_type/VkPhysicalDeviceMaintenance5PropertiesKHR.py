import ctypes

class VkPhysicalDeviceMaintenance5PropertiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'earlyFragmentMultisampleCoverageAfterSampleCounting': ctypes.c_uint32,
            'earlyFragmentSampleMaskTestBeforeSampleCounting': ctypes.c_uint32,
            'depthStencilSwizzleOneSupport': ctypes.c_uint32,
            'polygonModePointSize': ctypes.c_uint32,
            'nonStrictSinglePixelWideLinesUseParallelogram': ctypes.c_uint32,
            'nonStrictWideLinesUseParallelogram': ctypes.c_uint32,
        }

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
