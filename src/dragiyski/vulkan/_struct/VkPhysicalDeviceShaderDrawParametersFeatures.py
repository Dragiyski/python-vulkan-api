import ctypes, sys

class VkPhysicalDeviceShaderDrawParametersFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderDrawParameters', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderDrawParametersFeatures
