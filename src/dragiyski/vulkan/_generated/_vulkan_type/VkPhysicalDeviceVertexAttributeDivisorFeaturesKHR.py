import ctypes, sys

class VkPhysicalDeviceVertexAttributeDivisorFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vertexAttributeInstanceRateDivisor', ctypes.c_uint32),
        ('vertexAttributeInstanceRateZeroDivisor', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceVertexAttributeDivisorFeaturesKHR
