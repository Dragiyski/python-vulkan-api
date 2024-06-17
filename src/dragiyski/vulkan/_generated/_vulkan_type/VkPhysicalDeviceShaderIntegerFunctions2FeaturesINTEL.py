import ctypes, sys

class VkPhysicalDeviceShaderIntegerFunctions2FeaturesINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderIntegerFunctions2', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderIntegerFunctions2FeaturesINTEL
