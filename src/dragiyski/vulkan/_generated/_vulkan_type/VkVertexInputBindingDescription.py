import ctypes

class VkVertexInputBindingDescription(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('inputRate', ctypes.c_int),
    ]

VkVertexInputBindingDescription._type_ = {
    'binding': ctypes.c_uint32,
    'stride': ctypes.c_uint32,
    'inputRate': ctypes.c_int,
}
