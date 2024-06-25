import ctypes

class VkExportSemaphoreWin32HandleInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pAttributes', ctypes.c_void_p),
        ('dwAccess', ctypes.c_uint32),
        ('name', ctypes.c_wchar_p),
    ]

VkExportSemaphoreWin32HandleInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pAttributes': ctypes.c_void_p,
    'dwAccess': ctypes.c_uint32,
    'name': ctypes.c_wchar_p,
}
