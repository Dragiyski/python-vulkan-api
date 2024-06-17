import ctypes, sys

class VkVideoEncodeH265QpKHR(ctypes.Structure):
    _fields_ = [
        ('qpI', ctypes.c_int32),
        ('qpP', ctypes.c_int32),
        ('qpB', ctypes.c_int32),
    ]

sys.modules[__name__] = VkVideoEncodeH265QpKHR
