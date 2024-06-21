import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('pipelineMemorySize', ctypes.c_uint64),
        ('jsonSize', ctypes.c_uint64),
        ('jsonOffset', ctypes.c_uint64),
        ('stageIndexCount', ctypes.c_uint32),
        ('stageIndexStride', ctypes.c_uint32),
        ('stageIndexOffset', ctypes.c_uint64),
    ]
