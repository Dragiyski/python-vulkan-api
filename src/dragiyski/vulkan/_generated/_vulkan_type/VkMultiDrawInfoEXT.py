import ctypes, sys

class VkMultiDrawInfoEXT(ctypes.Structure):
    _fields_ = [
        ('firstVertex', ctypes.c_uint32),
        ('vertexCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMultiDrawInfoEXT
