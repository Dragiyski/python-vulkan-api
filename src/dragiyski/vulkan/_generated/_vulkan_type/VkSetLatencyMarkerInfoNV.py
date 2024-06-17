import ctypes, sys

class VkSetLatencyMarkerInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentID', ctypes.c_uint64),
        ('marker', ctypes.c_int),
    ]

sys.modules[__name__] = VkSetLatencyMarkerInfoNV
