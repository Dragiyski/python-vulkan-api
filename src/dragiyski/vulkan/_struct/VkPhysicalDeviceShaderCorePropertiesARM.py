import ctypes, sys

class VkPhysicalDeviceShaderCorePropertiesARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pixelRate', ctypes.c_uint32),
        ('texelRate', ctypes.c_uint32),
        ('fmaRate', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderCorePropertiesARM
