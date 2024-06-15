import ctypes, sys

class VkPhysicalDeviceShaderCoreBuiltinsPropertiesARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreMask', ctypes.c_uint64),
        ('shaderCoreCount', ctypes.c_uint32),
        ('shaderWarpsPerCore', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderCoreBuiltinsPropertiesARM
