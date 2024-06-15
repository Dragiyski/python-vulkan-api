import ctypes, sys

class VkImportMemoryHostPointerInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('pHostPointer', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkImportMemoryHostPointerInfoEXT
