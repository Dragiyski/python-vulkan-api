import ctypes, sys

class VkShaderModuleIdentifierEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('identifierSize', ctypes.c_uint32),
        ('identifier', ctypes.ARRAY(ctypes.c_uint8, 32)),
    ]

sys.modules[__name__] = VkShaderModuleIdentifierEXT
