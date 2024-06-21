import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('postMergeSubpassCount', ctypes.c_uint32),
    ]
