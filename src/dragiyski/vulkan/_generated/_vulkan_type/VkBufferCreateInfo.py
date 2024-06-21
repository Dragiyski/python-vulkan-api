import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('size', ctypes.c_uint64),
        ('usage', ctypes.c_uint32),
        ('sharingMode', ctypes.c_int),
        ('queueFamilyIndexCount', ctypes.c_uint32),
        ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]
