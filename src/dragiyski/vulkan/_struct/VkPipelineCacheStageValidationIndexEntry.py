import ctypes, sys

class VkPipelineCacheStageValidationIndexEntry(ctypes.Structure):
    _fields_ = [
        ('codeSize', ctypes.c_uint64),
        ('codeOffset', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPipelineCacheStageValidationIndexEntry
