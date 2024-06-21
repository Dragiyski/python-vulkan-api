import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxGraphicsShaderGroupCount', ctypes.c_uint32),
        ('maxIndirectSequenceCount', ctypes.c_uint32),
        ('maxIndirectCommandsTokenCount', ctypes.c_uint32),
        ('maxIndirectCommandsStreamCount', ctypes.c_uint32),
        ('maxIndirectCommandsTokenOffset', ctypes.c_uint32),
        ('maxIndirectCommandsStreamStride', ctypes.c_uint32),
        ('minSequencesCountBufferOffsetAlignment', ctypes.c_uint32),
        ('minSequencesIndexBufferOffsetAlignment', ctypes.c_uint32),
        ('minIndirectCommandsBufferOffsetAlignment', ctypes.c_uint32),
    ]
