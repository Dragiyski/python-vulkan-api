import ctypes, sys

class VkPhysicalDeviceToolProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('version', ctypes.ARRAY(ctypes.c_char, 256)),
        ('purposes', ctypes.c_uint32),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('layer', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

sys.modules[__name__] = VkPhysicalDeviceToolProperties
