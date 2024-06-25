import ctypes

class VkBufferDeviceAddressCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceAddress', ctypes.c_uint64),
    ]

VkBufferDeviceAddressCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceAddress': ctypes.c_uint64,
}
