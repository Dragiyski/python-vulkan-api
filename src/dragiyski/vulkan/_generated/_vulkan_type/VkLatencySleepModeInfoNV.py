import ctypes, sys

class VkLatencySleepModeInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('lowLatencyMode', ctypes.c_uint32),
        ('lowLatencyBoost', ctypes.c_uint32),
        ('minimumIntervalUs', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkLatencySleepModeInfoNV
