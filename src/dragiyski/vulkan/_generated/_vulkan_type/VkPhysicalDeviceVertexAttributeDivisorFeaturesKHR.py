import ctypes

class VkPhysicalDeviceVertexAttributeDivisorFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vertexAttributeInstanceRateDivisor', ctypes.c_uint32),
        ('vertexAttributeInstanceRateZeroDivisor', ctypes.c_uint32),
    ]

VkPhysicalDeviceVertexAttributeDivisorFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vertexAttributeInstanceRateDivisor': ctypes.c_uint32,
    'vertexAttributeInstanceRateZeroDivisor': ctypes.c_uint32,
}
