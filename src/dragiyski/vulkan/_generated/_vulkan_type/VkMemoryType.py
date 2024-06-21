import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('propertyFlags', ctypes.c_uint32),
        ('heapIndex', ctypes.c_uint32),
    ]
