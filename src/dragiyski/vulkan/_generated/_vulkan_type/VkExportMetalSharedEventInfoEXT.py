import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('event', ctypes.c_void_p),
        ('mtlSharedEvent', ctypes.c_void_p),
    ]
