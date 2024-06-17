import ctypes, sys

class VkPipelineCacheSafetyCriticalIndexEntry(ctypes.Structure):
    _fields_ = [
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('pipelineMemorySize', ctypes.c_uint64),
        ('jsonSize', ctypes.c_uint64),
        ('jsonOffset', ctypes.c_uint64),
        ('stageIndexCount', ctypes.c_uint32),
        ('stageIndexStride', ctypes.c_uint32),
        ('stageIndexOffset', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPipelineCacheSafetyCriticalIndexEntry
