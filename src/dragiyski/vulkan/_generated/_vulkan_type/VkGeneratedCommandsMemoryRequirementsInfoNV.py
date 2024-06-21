import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineBindPoint', ctypes.c_int),
        ('pipeline', ctypes.c_void_p),
        ('indirectCommandsLayout', ctypes.c_void_p),
        ('maxSequencesCount', ctypes.c_uint32),
    ]
