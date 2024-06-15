import ctypes, sys

class VkDepthBiasInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasConstantFactor', ctypes.c_float),
        ('depthBiasClamp', ctypes.c_float),
        ('depthBiasSlopeFactor', ctypes.c_float),
    ]

sys.modules[__name__] = VkDepthBiasInfoEXT
