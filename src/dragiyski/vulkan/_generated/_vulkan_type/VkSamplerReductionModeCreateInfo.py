import ctypes, sys

class VkSamplerReductionModeCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('reductionMode', ctypes.c_int),
    ]

sys.modules[__name__] = VkSamplerReductionModeCreateInfo
