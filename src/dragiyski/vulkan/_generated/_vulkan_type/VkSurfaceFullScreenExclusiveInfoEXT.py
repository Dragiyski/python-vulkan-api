import ctypes, sys

class VkSurfaceFullScreenExclusiveInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fullScreenExclusive', ctypes.c_int),
    ]

sys.modules[__name__] = VkSurfaceFullScreenExclusiveInfoEXT
