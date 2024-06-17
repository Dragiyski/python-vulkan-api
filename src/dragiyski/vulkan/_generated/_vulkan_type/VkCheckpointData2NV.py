import ctypes, sys

class VkCheckpointData2NV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stage', ctypes.c_uint64),
        ('pCheckpointMarker', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkCheckpointData2NV
