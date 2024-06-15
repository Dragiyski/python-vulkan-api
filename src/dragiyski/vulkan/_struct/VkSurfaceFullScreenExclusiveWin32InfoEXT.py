import ctypes, sys

class VkSurfaceFullScreenExclusiveWin32InfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hmonitor', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkSurfaceFullScreenExclusiveWin32InfoEXT
