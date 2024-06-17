import ctypes, sys

class VkPushConstantsInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('layout', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
        ('pValues', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkPushConstantsInfoKHR
