import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('formatA4R4G4B4', ctypes.c_uint32),
        ('formatA4B4G4R4', ctypes.c_uint32),
    ]
