import ctypes, sys

class VkPhysicalDeviceShaderFloat16Int8Features(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderFloat16', ctypes.c_uint32),
        ('shaderInt8', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderFloat16Int8Features
