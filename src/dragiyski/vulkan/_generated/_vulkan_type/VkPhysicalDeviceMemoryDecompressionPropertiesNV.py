import ctypes, sys

class VkPhysicalDeviceMemoryDecompressionPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('decompressionMethods', ctypes.c_uint64),
        ('maxDecompressionIndirectCount', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPhysicalDeviceMemoryDecompressionPropertiesNV
