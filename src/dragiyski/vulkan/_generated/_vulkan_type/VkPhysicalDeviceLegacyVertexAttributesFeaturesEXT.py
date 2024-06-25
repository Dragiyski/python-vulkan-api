import ctypes

class VkPhysicalDeviceLegacyVertexAttributesFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('legacyVertexAttributes', ctypes.c_uint32),
    ]

VkPhysicalDeviceLegacyVertexAttributesFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'legacyVertexAttributes': ctypes.c_uint32,
}
