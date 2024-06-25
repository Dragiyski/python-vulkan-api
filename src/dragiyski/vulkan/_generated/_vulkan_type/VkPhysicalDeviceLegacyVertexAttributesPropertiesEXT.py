import ctypes

class VkPhysicalDeviceLegacyVertexAttributesPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('nativeUnalignedPerformance', ctypes.c_uint32),
    ]

VkPhysicalDeviceLegacyVertexAttributesPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'nativeUnalignedPerformance': ctypes.c_uint32,
}
