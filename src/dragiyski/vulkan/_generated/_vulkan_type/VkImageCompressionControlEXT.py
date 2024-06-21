import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('compressionControlPlaneCount', ctypes.c_uint32),
        ('pFixedRateFlags', ctypes.POINTER(ctypes.c_uint32)),
    ]
