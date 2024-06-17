import ctypes, sys

class VkDeviceEventInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceEvent', ctypes.c_int),
    ]

sys.modules[__name__] = VkDeviceEventInfoEXT
