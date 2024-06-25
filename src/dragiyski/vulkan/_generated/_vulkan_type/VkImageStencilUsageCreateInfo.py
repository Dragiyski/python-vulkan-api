import ctypes

class VkImageStencilUsageCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stencilUsage', ctypes.c_uint32),
    ]

VkImageStencilUsageCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stencilUsage': ctypes.c_uint32,
}
