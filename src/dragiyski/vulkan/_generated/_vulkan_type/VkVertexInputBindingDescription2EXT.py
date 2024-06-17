import ctypes, sys

class VkVertexInputBindingDescription2EXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('binding', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('inputRate', ctypes.c_int),
        ('divisor', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVertexInputBindingDescription2EXT
