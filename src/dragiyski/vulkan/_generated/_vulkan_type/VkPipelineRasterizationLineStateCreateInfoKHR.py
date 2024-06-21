import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('lineRasterizationMode', ctypes.c_int),
        ('stippledLineEnable', ctypes.c_uint32),
        ('lineStippleFactor', ctypes.c_uint32),
        ('lineStipplePattern', ctypes.c_uint16),
    ]
