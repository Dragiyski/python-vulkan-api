import ctypes, sys

class VkPhysicalDeviceShaderFloatControls2FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderFloatControls2', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderFloatControls2FeaturesKHR
