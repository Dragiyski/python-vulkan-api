import ctypes, sys

class VkExportMetalSharedEventInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('event', ctypes.c_void_p),
        ('mtlSharedEvent', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkExportMetalSharedEventInfoEXT
