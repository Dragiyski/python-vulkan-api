import ctypes, sys

class VkPhysicalDeviceShaderTerminateInvocationFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderTerminateInvocation', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderTerminateInvocationFeatures
