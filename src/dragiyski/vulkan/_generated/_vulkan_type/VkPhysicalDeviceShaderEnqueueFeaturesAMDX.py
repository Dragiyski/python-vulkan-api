import ctypes, sys

class VkPhysicalDeviceShaderEnqueueFeaturesAMDX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderEnqueue', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderEnqueueFeaturesAMDX
