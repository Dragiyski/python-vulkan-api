import ctypes

class VkPhysicalDeviceVertexAttributeDivisorPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxVertexAttribDivisor', ctypes.c_uint32),
        ('supportsNonZeroFirstInstance', ctypes.c_uint32),
    ]

VkPhysicalDeviceVertexAttributeDivisorPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxVertexAttribDivisor': ctypes.c_uint32,
    'supportsNonZeroFirstInstance': ctypes.c_uint32,
}
