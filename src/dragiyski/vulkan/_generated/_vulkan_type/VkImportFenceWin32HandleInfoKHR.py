import ctypes

class VkImportFenceWin32HandleInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'fence': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'handleType': ctypes.c_uint32,
            'handle': ctypes.c_void_p,
            'name': ctypes.c_wchar_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fence', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_void_p),
        ('name', ctypes.c_wchar_p),
    ]
