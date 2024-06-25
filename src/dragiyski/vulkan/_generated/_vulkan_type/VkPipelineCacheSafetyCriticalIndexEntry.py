import ctypes

class VkPipelineCacheSafetyCriticalIndexEntry(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'pipelineIdentifier': ctypes.ARRAY(ctypes.c_uint8, 16),
            'pipelineMemorySize': ctypes.c_uint64,
            'jsonSize': ctypes.c_uint64,
            'jsonOffset': ctypes.c_uint64,
            'stageIndexCount': ctypes.c_uint32,
            'stageIndexStride': ctypes.c_uint32,
            'stageIndexOffset': ctypes.c_uint64,
        }

    _fields_ = [
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('pipelineMemorySize', ctypes.c_uint64),
        ('jsonSize', ctypes.c_uint64),
        ('jsonOffset', ctypes.c_uint64),
        ('stageIndexCount', ctypes.c_uint32),
        ('stageIndexStride', ctypes.c_uint32),
        ('stageIndexOffset', ctypes.c_uint64),
    ]
