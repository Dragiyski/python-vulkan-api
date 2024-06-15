import ctypes, sys

class VkPipelineCoverageReductionStateCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('coverageReductionMode', ctypes.c_int),
    ]

sys.modules[__name__] = VkPipelineCoverageReductionStateCreateInfoNV
