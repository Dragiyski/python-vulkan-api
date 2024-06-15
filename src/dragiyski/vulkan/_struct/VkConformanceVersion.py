import ctypes, sys

class VkConformanceVersion(ctypes.Structure):
    _fields_ = [
        ('major', ctypes.c_uint8),
        ('minor', ctypes.c_uint8),
        ('subminor', ctypes.c_uint8),
        ('patch', ctypes.c_uint8),
    ]

sys.modules[__name__] = VkConformanceVersion
