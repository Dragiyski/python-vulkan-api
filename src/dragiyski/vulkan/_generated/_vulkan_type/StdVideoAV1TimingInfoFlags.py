import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('equal_picture_interval', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]
