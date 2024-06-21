import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('usage', ctypes.c_uint32),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
        ('viewFormatCount', ctypes.c_uint32),
        ('pViewFormats', ctypes.POINTER(ctypes.c_int)),
    ]
