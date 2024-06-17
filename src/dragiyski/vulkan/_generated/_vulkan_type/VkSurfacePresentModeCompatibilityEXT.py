import ctypes, sys

class VkSurfacePresentModeCompatibilityEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentModeCount', ctypes.c_uint32),
        ('pPresentModes', ctypes.POINTER(ctypes.c_int)),
    ]

sys.modules[__name__] = VkSurfacePresentModeCompatibilityEXT
