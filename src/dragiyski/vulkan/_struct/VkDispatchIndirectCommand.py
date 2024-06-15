import ctypes, sys

class VkDispatchIndirectCommand(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_uint32),
        ('y', ctypes.c_uint32),
        ('z', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDispatchIndirectCommand
