import ctypes, sys

class VkFrameBoundaryEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('frameID', ctypes.c_uint64),
        ('imageCount', ctypes.c_uint32),
        ('pImages', ctypes.POINTER(ctypes.c_void_p)),
        ('bufferCount', ctypes.c_uint32),
        ('pBuffers', ctypes.POINTER(ctypes.c_void_p)),
        ('tagName', ctypes.c_uint64),
        ('tagSize', ctypes.c_size_t),
        ('pTag', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkFrameBoundaryEXT
