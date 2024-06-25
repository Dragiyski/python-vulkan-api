import ctypes

class VkVideoEncodeH264FrameSizeKHR(ctypes.Structure):
    _fields_ = [
        ('frameISize', ctypes.c_uint32),
        ('framePSize', ctypes.c_uint32),
        ('frameBSize', ctypes.c_uint32),
    ]

VkVideoEncodeH264FrameSizeKHR._type_ = {
    'frameISize': ctypes.c_uint32,
    'framePSize': ctypes.c_uint32,
    'frameBSize': ctypes.c_uint32,
}
