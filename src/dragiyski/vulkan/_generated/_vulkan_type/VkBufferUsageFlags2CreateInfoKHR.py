import ctypes

class VkBufferUsageFlags2CreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('usage', ctypes.c_uint64),
    ]

VkBufferUsageFlags2CreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'usage': ctypes.c_uint64,
}
