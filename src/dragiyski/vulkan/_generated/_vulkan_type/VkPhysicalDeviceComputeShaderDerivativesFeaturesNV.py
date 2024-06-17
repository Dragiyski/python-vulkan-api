import ctypes, sys

class VkPhysicalDeviceComputeShaderDerivativesFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('computeDerivativeGroupQuads', ctypes.c_uint32),
        ('computeDerivativeGroupLinear', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceComputeShaderDerivativesFeaturesNV
