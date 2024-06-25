import ctypes

class VkDebugMarkerObjectTagInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('objectType', ctypes.c_int),
        ('object', ctypes.c_uint64),
        ('tagName', ctypes.c_uint64),
        ('tagSize', ctypes.c_size_t),
        ('pTag', ctypes.c_void_p),
    ]

VkDebugMarkerObjectTagInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'objectType': ctypes.c_int,
    'object': ctypes.c_uint64,
    'tagName': ctypes.c_uint64,
    'tagSize': ctypes.c_size_t,
    'pTag': ctypes.c_void_p,
}
