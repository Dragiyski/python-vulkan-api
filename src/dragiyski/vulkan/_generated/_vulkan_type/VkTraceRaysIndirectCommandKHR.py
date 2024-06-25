import ctypes

class VkTraceRaysIndirectCommandKHR(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('depth', ctypes.c_uint32),
    ]

VkTraceRaysIndirectCommandKHR._type_ = {
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
    'depth': ctypes.c_uint32,
}
