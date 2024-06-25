import ctypes

class VkExportSemaphoreSciSyncInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pAttributes', ctypes.c_void_p),
    ]

VkExportSemaphoreSciSyncInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pAttributes': ctypes.c_void_p,
}
