import ctypes

class VkExternalFormatANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('externalFormat', ctypes.c_uint64),
    ]

VkExternalFormatANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'externalFormat': ctypes.c_uint64,
}
