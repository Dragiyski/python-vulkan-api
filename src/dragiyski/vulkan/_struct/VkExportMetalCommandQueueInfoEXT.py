import ctypes, sys

class VkExportMetalCommandQueueInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queue', ctypes.c_void_p),
        ('mtlCommandQueue', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkExportMetalCommandQueueInfoEXT
