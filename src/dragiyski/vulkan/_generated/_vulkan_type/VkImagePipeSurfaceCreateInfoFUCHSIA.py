import ctypes

class VkImagePipeSurfaceCreateInfoFUCHSIA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('imagePipeHandle', ctypes.c_uint32),
    ]

VkImagePipeSurfaceCreateInfoFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'imagePipeHandle': ctypes.c_uint32,
}
