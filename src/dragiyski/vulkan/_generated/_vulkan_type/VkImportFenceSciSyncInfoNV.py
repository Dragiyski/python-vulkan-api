import ctypes

class VkImportFenceSciSyncInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fence', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_void_p),
    ]

VkImportFenceSciSyncInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fence': ctypes.c_void_p,
    'handleType': ctypes.c_uint32,
    'handle': ctypes.c_void_p,
}
