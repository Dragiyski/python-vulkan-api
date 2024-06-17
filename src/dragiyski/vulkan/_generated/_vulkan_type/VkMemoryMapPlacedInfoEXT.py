import ctypes, sys

class VkMemoryMapPlacedInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pPlacedAddress', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkMemoryMapPlacedInfoEXT
