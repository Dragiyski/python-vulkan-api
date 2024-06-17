import ctypes, sys

class VkPhysicalDeviceVertexAttributeDivisorPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxVertexAttribDivisor', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceVertexAttributeDivisorPropertiesEXT
