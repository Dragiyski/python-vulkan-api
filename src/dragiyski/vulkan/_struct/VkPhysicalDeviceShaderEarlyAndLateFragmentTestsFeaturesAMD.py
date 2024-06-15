import ctypes, sys

class VkPhysicalDeviceShaderEarlyAndLateFragmentTestsFeaturesAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderEarlyAndLateFragmentTests', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderEarlyAndLateFragmentTestsFeaturesAMD
