import ctypes

class VkBufferOpaqueCaptureAddressCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('opaqueCaptureAddress', ctypes.c_uint64),
    ]

VkBufferOpaqueCaptureAddressCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'opaqueCaptureAddress': ctypes.c_uint64,
}
