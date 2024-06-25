import ctypes

class VkVideoEncodeH265FrameSizeKHR(ctypes.Structure):
    _fields_ = [
        ('frameISize', ctypes.c_uint32),
        ('framePSize', ctypes.c_uint32),
        ('frameBSize', ctypes.c_uint32),
    ]

VkVideoEncodeH265FrameSizeKHR._type_ = {
    'frameISize': ctypes.c_uint32,
    'framePSize': ctypes.c_uint32,
    'frameBSize': ctypes.c_uint32,
}
