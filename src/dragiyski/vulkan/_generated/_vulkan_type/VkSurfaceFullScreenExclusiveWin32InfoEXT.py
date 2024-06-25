import ctypes

class VkSurfaceFullScreenExclusiveWin32InfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hmonitor', ctypes.c_void_p),
    ]

VkSurfaceFullScreenExclusiveWin32InfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'hmonitor': ctypes.c_void_p,
}
