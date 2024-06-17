import ctypes, sys

class VkImagePlaneMemoryRequirementsInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('planeAspect', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkImagePlaneMemoryRequirementsInfo
