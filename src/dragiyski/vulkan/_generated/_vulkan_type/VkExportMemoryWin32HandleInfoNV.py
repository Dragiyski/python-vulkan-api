import ctypes

class VkExportMemoryWin32HandleInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pAttributes', ctypes.c_void_p),
        ('dwAccess', ctypes.c_uint32),
    ]

VkExportMemoryWin32HandleInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pAttributes': ctypes.c_void_p,
    'dwAccess': ctypes.c_uint32,
}
