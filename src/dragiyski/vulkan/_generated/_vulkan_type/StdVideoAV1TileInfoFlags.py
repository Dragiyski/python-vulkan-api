import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('uniform_tile_spacing_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]
