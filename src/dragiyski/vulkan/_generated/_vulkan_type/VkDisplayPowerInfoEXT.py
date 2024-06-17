import ctypes, sys

class VkDisplayPowerInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('powerState', ctypes.c_int),
    ]

sys.modules[__name__] = VkDisplayPowerInfoEXT
