import ctypes

class VkSamplerCubicWeightsCreateInfoQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cubicWeights', ctypes.c_int),
    ]

VkSamplerCubicWeightsCreateInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'cubicWeights': ctypes.c_int,
}
