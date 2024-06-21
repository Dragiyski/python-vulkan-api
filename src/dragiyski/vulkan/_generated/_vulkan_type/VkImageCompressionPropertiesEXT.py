import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageCompressionFlags', ctypes.c_uint32),
        ('imageCompressionFixedRateFlags', ctypes.c_uint32),
    ]
