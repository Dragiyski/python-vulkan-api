import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('subpassMergeStatus', ctypes.c_int),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('postMergeIndex', ctypes.c_uint32),
    ]
