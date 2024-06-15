import ctypes, sys

class VkMultiDrawIndexedInfoEXT(ctypes.Structure):
    _fields_ = [
        ('firstIndex', ctypes.c_uint32),
        ('indexCount', ctypes.c_uint32),
        ('vertexOffset', ctypes.c_int32),
    ]

sys.modules[__name__] = VkMultiDrawIndexedInfoEXT
