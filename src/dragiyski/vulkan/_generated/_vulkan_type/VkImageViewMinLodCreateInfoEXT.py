import ctypes

class VkImageViewMinLodCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minLod', ctypes.c_float),
    ]

VkImageViewMinLodCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'minLod': ctypes.c_float,
}
