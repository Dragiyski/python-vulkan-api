import ctypes, sys

class VkDisplayEventInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('displayEvent', ctypes.c_int),
    ]

sys.modules[__name__] = VkDisplayEventInfoEXT
