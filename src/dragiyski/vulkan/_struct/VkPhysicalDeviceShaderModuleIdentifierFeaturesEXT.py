import ctypes, sys

class VkPhysicalDeviceShaderModuleIdentifierFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderModuleIdentifier', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderModuleIdentifierFeaturesEXT
