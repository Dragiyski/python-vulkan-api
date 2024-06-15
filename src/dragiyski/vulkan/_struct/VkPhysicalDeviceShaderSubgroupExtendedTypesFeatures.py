import ctypes, sys

class VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderSubgroupExtendedTypes', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures
