import ctypes, sys

class VkCheckpointDataNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stage', ctypes.c_uint32),
        ('pCheckpointMarker', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkCheckpointDataNV
