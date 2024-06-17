import ctypes, sys

class VkMicromapUsageEXT(ctypes.Structure):
    _fields_ = [
        ('count', ctypes.c_uint32),
        ('subdivisionLevel', ctypes.c_uint32),
        ('format', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMicromapUsageEXT
