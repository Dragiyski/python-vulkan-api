import ctypes, sys

class VkPipelineShaderStageModuleIdentifierCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('identifierSize', ctypes.c_uint32),
        ('pIdentifier', ctypes.POINTER(ctypes.c_uint8)),
    ]

sys.modules[__name__] = VkPipelineShaderStageModuleIdentifierCreateInfoEXT
