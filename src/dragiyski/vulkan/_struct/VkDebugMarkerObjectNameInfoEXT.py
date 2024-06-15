import ctypes, sys

class VkDebugMarkerObjectNameInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('objectType', ctypes.c_int),
        ('object', ctypes.c_uint64),
        ('pObjectName', ctypes.c_char_p),
    ]

sys.modules[__name__] = VkDebugMarkerObjectNameInfoEXT
