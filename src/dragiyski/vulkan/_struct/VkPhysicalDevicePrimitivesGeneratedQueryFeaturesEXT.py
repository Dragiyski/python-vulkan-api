import ctypes, sys

class VkPhysicalDevicePrimitivesGeneratedQueryFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitivesGeneratedQuery', ctypes.c_uint32),
        ('primitivesGeneratedQueryWithRasterizerDiscard', ctypes.c_uint32),
        ('primitivesGeneratedQueryWithNonZeroStreams', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePrimitivesGeneratedQueryFeaturesEXT