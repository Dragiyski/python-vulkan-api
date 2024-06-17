import ctypes, sys

class VkVideoEncodeH264FrameSizeKHR(ctypes.Structure):
    _fields_ = [
        ('frameISize', ctypes.c_uint32),
        ('framePSize', ctypes.c_uint32),
        ('frameBSize', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoEncodeH264FrameSizeKHR
