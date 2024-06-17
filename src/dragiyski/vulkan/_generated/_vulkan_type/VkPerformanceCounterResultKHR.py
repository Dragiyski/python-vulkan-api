import ctypes, sys

class VkPerformanceCounterResultKHR(ctypes.Union):
    _fields_ = [
        ('int32', ctypes.c_int32),
        ('int64', ctypes.c_int64),
        ('uint32', ctypes.c_uint32),
        ('uint64', ctypes.c_uint64),
        ('float32', ctypes.c_float),
        ('float64', ctypes.c_double),
    ]

sys.modules[__name__] = VkPerformanceCounterResultKHR
