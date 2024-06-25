import ctypes

class VkPipelineShaderStageModuleIdentifierCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('identifierSize', ctypes.c_uint32),
        ('pIdentifier', ctypes.POINTER(ctypes.c_uint8)),
    ]

VkPipelineShaderStageModuleIdentifierCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'identifierSize': ctypes.c_uint32,
    'pIdentifier': ctypes.POINTER(ctypes.c_uint8),
}
