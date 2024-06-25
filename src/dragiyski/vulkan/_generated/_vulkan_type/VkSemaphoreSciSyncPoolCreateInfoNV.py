import ctypes

class VkSemaphoreSciSyncPoolCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handle', ctypes.c_void_p),
    ]

VkSemaphoreSciSyncPoolCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'handle': ctypes.c_void_p,
}
