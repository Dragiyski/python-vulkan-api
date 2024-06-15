import ctypes, sys

class VkPhysicalDeviceLegacyVertexAttributesFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('legacyVertexAttributes', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceLegacyVertexAttributesFeaturesEXT
