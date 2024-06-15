import ctypes, sys

class VkSurfaceCapabilitiesFullScreenExclusiveEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fullScreenExclusiveSupported', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSurfaceCapabilitiesFullScreenExclusiveEXT
