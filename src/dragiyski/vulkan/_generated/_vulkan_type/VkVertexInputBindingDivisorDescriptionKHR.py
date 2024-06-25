import ctypes

class VkVertexInputBindingDivisorDescriptionKHR(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('divisor', ctypes.c_uint32),
    ]

VkVertexInputBindingDivisorDescriptionKHR._type_ = {
    'binding': ctypes.c_uint32,
    'divisor': ctypes.c_uint32,
}
