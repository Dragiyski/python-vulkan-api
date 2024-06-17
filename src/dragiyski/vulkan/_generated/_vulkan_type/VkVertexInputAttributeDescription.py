import ctypes, sys

class VkVertexInputAttributeDescription(ctypes.Structure):
    _fields_ = [
        ('location', ctypes.c_uint32),
        ('binding', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVertexInputAttributeDescription
