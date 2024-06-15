import ctypes, sys

class VkBufferUsageFlags2CreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('usage', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkBufferUsageFlags2CreateInfoKHR
