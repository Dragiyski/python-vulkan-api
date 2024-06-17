import ctypes, sys

class VkVertexInputBindingDivisorDescriptionKHR(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('divisor', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVertexInputBindingDivisorDescriptionKHR
