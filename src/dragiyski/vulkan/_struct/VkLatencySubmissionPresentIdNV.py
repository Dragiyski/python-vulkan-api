import ctypes, sys

class VkLatencySubmissionPresentIdNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentID', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkLatencySubmissionPresentIdNV
