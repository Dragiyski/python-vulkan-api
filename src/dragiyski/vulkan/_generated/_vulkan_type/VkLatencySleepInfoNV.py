import ctypes

class VkLatencySleepInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('signalSemaphore', ctypes.c_void_p),
        ('value', ctypes.c_uint64),
    ]

VkLatencySleepInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'signalSemaphore': ctypes.c_void_p,
    'value': ctypes.c_uint64,
}
