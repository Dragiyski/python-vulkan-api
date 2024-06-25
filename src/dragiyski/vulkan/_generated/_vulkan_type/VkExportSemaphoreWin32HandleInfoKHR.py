import ctypes

class VkExportSemaphoreWin32HandleInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pAttributes': ctypes.c_void_p,
            'dwAccess': ctypes.c_uint32,
            'name': ctypes.c_wchar_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pAttributes', ctypes.c_void_p),
        ('dwAccess', ctypes.c_uint32),
        ('name', ctypes.c_wchar_p),
    ]
