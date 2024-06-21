import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('perViewAttributes', ctypes.c_uint32),
        ('perViewAttributesPositionXOnly', ctypes.c_uint32),
    ]
