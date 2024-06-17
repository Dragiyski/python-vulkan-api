import ctypes, sys

class VkPhysicalDeviceCoverageReductionModeFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('coverageReductionMode', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceCoverageReductionModeFeaturesNV
