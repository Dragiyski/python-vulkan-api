import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queueFamilyIndex', ctypes.c_uint32),
        ('counterIndexCount', ctypes.c_uint32),
        ('pCounterIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]