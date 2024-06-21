import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceFault', ctypes.c_uint32),
        ('deviceFaultVendorBinary', ctypes.c_uint32),
    ]
