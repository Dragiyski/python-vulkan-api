import ctypes

class VkPhysicalDevicePresentationPropertiesANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sharedImage', ctypes.c_uint32),
    ]

VkPhysicalDevicePresentationPropertiesANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sharedImage': ctypes.c_uint32,
}
