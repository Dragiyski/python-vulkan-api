import ctypes

class VkSurfacePresentModeEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentMode', ctypes.c_int),
    ]

VkSurfacePresentModeEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentMode': ctypes.c_int,
}
