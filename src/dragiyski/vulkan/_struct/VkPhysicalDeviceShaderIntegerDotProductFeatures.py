import ctypes, sys

class VkPhysicalDeviceShaderIntegerDotProductFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderIntegerDotProduct', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderIntegerDotProductFeatures
