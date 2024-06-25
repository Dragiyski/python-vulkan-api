import ctypes

class VkVideoEncodeH265GopRemainingFrameInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('useGopRemainingFrames', ctypes.c_uint32),
        ('gopRemainingI', ctypes.c_uint32),
        ('gopRemainingP', ctypes.c_uint32),
        ('gopRemainingB', ctypes.c_uint32),
    ]

VkVideoEncodeH265GopRemainingFrameInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'useGopRemainingFrames': ctypes.c_uint32,
    'gopRemainingI': ctypes.c_uint32,
    'gopRemainingP': ctypes.c_uint32,
    'gopRemainingB': ctypes.c_uint32,
}
