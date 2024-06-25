import ctypes

class VkPhysicalDeviceShaderModuleIdentifierPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderModuleIdentifierAlgorithmUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]

VkPhysicalDeviceShaderModuleIdentifierPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderModuleIdentifierAlgorithmUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
}
