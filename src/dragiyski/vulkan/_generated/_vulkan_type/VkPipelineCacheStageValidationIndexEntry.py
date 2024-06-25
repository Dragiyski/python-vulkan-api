import ctypes

class VkPipelineCacheStageValidationIndexEntry(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'codeSize': ctypes.c_uint64,
            'codeOffset': ctypes.c_uint64,
        }

    _fields_ = [
        ('codeSize', ctypes.c_uint64),
        ('codeOffset', ctypes.c_uint64),
    ]
