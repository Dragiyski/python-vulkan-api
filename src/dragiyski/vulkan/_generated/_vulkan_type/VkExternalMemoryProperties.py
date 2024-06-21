import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('externalMemoryFeatures', ctypes.c_uint32),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
    ]
