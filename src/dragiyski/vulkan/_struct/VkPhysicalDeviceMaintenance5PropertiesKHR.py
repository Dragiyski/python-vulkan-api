import ctypes, sys

class VkPhysicalDeviceMaintenance5PropertiesKHR(ctypes.Structure):
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

sys.modules[__name__] = VkPhysicalDeviceMaintenance5PropertiesKHR
