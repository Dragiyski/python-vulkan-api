import ctypes, sys

class VkPhysicalDevicePresentationPropertiesANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sharedImage', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePresentationPropertiesANDROID
