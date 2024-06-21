import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustStorageBufferAccessSizeAlignment', ctypes.c_uint64),
        ('robustUniformBufferAccessSizeAlignment', ctypes.c_uint64),
    ]
