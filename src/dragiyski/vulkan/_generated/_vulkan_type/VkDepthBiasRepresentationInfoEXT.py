import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasRepresentation', ctypes.c_int),
        ('depthBiasExact', ctypes.c_uint32),
    ]
