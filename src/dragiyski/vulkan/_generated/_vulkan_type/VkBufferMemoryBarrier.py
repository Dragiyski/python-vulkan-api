import ctypes

class VkBufferMemoryBarrier(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
        ('srcQueueFamilyIndex', ctypes.c_uint32),
        ('dstQueueFamilyIndex', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

VkBufferMemoryBarrier._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcAccessMask': ctypes.c_uint32,
    'dstAccessMask': ctypes.c_uint32,
    'srcQueueFamilyIndex': ctypes.c_uint32,
    'dstQueueFamilyIndex': ctypes.c_uint32,
    'buffer': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
