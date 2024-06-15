import ctypes, sys

class VkPhysicalDeviceShaderCoreProperties2AMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreFeatures', ctypes.c_uint32),
        ('activeComputeUnitCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderCoreProperties2AMD
