import ctypes

class VkImageViewAddressPropertiesNVX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

VkImageViewAddressPropertiesNVX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceAddress': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
