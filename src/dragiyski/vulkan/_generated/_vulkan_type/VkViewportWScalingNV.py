import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('xcoeff', ctypes.c_float),
        ('ycoeff', ctypes.c_float),
    ]
