import ctypes, sys

class VkImportMetalSharedEventInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mtlSharedEvent', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkImportMetalSharedEventInfoEXT
