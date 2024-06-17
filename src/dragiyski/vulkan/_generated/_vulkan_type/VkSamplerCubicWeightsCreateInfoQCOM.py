import ctypes, sys

class VkSamplerCubicWeightsCreateInfoQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cubicWeights', ctypes.c_int),
    ]

sys.modules[__name__] = VkSamplerCubicWeightsCreateInfoQCOM
