import ctypes

class VkSubresourceHostMemcpySizeEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('size', ctypes.c_uint64),
    ]

VkSubresourceHostMemcpySizeEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'size': ctypes.c_uint64,
}
