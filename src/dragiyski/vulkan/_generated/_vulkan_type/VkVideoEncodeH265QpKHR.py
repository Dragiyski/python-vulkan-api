import ctypes

class VkVideoEncodeH265QpKHR(ctypes.Structure):
    _fields_ = [
        ('qpI', ctypes.c_int32),
        ('qpP', ctypes.c_int32),
        ('qpB', ctypes.c_int32),
    ]

VkVideoEncodeH265QpKHR._type_ = {
    'qpI': ctypes.c_int32,
    'qpP': ctypes.c_int32,
    'qpB': ctypes.c_int32,
}
