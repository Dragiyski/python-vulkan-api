import ctypes

class VkMemoryMapPlacedInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pPlacedAddress', ctypes.c_void_p),
    ]

VkMemoryMapPlacedInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pPlacedAddress': ctypes.c_void_p,
}
