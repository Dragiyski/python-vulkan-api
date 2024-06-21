import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('pipelineAddress', ctypes.c_uint64),
    ]
