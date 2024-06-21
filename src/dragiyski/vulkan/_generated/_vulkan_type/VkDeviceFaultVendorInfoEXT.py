import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('vendorFaultCode', ctypes.c_uint64),
        ('vendorFaultData', ctypes.c_uint64),
    ]
