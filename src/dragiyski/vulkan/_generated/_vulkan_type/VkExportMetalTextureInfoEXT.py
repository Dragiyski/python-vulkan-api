import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('bufferView', ctypes.c_void_p),
        ('plane', ctypes.c_uint32),
        ('mtlTexture', ctypes.c_void_p),
    ]
