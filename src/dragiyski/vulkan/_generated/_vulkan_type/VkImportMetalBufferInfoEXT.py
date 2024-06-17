import ctypes, sys

class VkImportMetalBufferInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mtlBuffer', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkImportMetalBufferInfoEXT
