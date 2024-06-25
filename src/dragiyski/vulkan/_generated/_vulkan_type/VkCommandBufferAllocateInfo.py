import ctypes

class VkCommandBufferAllocateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandPool', ctypes.c_void_p),
        ('level', ctypes.c_int),
        ('commandBufferCount', ctypes.c_uint32),
    ]

VkCommandBufferAllocateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'commandPool': ctypes.c_void_p,
    'level': ctypes.c_int,
    'commandBufferCount': ctypes.c_uint32,
}
