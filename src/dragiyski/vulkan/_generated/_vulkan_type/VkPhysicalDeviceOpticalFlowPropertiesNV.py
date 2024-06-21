import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedOutputGridSizes', ctypes.c_uint32),
        ('supportedHintGridSizes', ctypes.c_uint32),
        ('hintSupported', ctypes.c_uint32),
        ('costSupported', ctypes.c_uint32),
        ('bidirectionalFlowSupported', ctypes.c_uint32),
        ('globalFlowSupported', ctypes.c_uint32),
        ('minWidth', ctypes.c_uint32),
        ('minHeight', ctypes.c_uint32),
        ('maxWidth', ctypes.c_uint32),
        ('maxHeight', ctypes.c_uint32),
        ('maxNumRegionsOfInterest', ctypes.c_uint32),
    ]