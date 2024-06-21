import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
        ('deviceIndexCount', ctypes.c_uint32),
        ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]
