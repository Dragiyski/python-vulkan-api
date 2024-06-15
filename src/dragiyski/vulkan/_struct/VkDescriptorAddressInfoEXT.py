import ctypes, sys

class VkDescriptorAddressInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('address', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
        ('format', ctypes.c_int),
    ]

sys.modules[__name__] = VkDescriptorAddressInfoEXT
