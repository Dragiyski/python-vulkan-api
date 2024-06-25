import ctypes

class VkPhysicalDeviceShaderModuleIdentifierFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderModuleIdentifier', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderModuleIdentifierFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderModuleIdentifier': ctypes.c_uint32,
}
