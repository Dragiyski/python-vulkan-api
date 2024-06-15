import ctypes, sys

class VkPhysicalDeviceShaderMaximalReconvergenceFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderMaximalReconvergence', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderMaximalReconvergenceFeaturesKHR
