import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryMapPlaced', ctypes.c_uint32),
        ('memoryMapRangePlaced', ctypes.c_uint32),
        ('memoryUnmapReserve', ctypes.c_uint32),
    ]
