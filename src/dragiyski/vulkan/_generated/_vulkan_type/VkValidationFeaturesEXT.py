import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('enabledValidationFeatureCount', ctypes.c_uint32),
        ('pEnabledValidationFeatures', ctypes.POINTER(ctypes.c_int)),
        ('disabledValidationFeatureCount', ctypes.c_uint32),
        ('pDisabledValidationFeatures', ctypes.POINTER(ctypes.c_int)),
    ]
