import ctypes, sys

class VkPhysicalDeviceShaderQuadControlFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderQuadControl', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderQuadControlFeaturesKHR
