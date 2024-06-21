import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('drmFormatModifier', ctypes.c_uint64),
        ('sharingMode', ctypes.c_int),
        ('queueFamilyIndexCount', ctypes.c_uint32),
        ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]
