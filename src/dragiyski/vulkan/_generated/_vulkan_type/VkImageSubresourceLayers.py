import ctypes

class VkImageSubresourceLayers(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('baseArrayLayer', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
    ]

VkImageSubresourceLayers._type_ = {
    'aspectMask': ctypes.c_uint32,
    'mipLevel': ctypes.c_uint32,
    'baseArrayLayer': ctypes.c_uint32,
    'layerCount': ctypes.c_uint32,
}
