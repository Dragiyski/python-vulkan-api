import ctypes, sys

class VkDisplayNativeHdrSurfaceCapabilitiesAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('localDimmingSupport', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDisplayNativeHdrSurfaceCapabilitiesAMD
