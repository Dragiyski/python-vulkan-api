import ctypes, sys

class VkPhysicalDeviceCubicWeightsFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('selectableCubicWeights', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceCubicWeightsFeaturesQCOM
