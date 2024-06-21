import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderModuleIdentifierAlgorithmUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]