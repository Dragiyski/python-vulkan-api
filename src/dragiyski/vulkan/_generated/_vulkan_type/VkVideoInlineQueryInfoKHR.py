import ctypes

class VkVideoInlineQueryInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queryPool', ctypes.c_void_p),
        ('firstQuery', ctypes.c_uint32),
        ('queryCount', ctypes.c_uint32),
    ]

VkVideoInlineQueryInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'queryPool': ctypes.c_void_p,
    'firstQuery': ctypes.c_uint32,
    'queryCount': ctypes.c_uint32,
}
