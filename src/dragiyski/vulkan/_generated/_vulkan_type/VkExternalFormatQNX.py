import ctypes

class VkExternalFormatQNX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('externalFormat', ctypes.c_uint64),
    ]

VkExternalFormatQNX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'externalFormat': ctypes.c_uint64,
}
