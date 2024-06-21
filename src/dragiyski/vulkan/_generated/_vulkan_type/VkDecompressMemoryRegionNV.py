import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('srcAddress', ctypes.c_uint64),
        ('dstAddress', ctypes.c_uint64),
        ('compressedSize', ctypes.c_uint64),
        ('decompressedSize', ctypes.c_uint64),
        ('decompressionMethod', ctypes.c_uint64),
    ]
