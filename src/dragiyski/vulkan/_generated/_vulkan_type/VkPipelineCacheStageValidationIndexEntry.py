import ctypes

class VkPipelineCacheStageValidationIndexEntry(ctypes.Structure):
    _fields_ = [
        ('codeSize', ctypes.c_uint64),
        ('codeOffset', ctypes.c_uint64),
    ]

VkPipelineCacheStageValidationIndexEntry._type_ = {
    'codeSize': ctypes.c_uint64,
    'codeOffset': ctypes.c_uint64,
}
