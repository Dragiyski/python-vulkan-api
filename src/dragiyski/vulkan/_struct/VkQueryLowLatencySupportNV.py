import ctypes, sys

class VkQueryLowLatencySupportNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pQueriedLowLatencyData', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkQueryLowLatencySupportNV
