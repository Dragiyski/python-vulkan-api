import ctypes

class VkBindPipelineIndirectCommandNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'pipelineAddress': ctypes.c_uint64,
        }

    _fields_ = [
        ('pipelineAddress', ctypes.c_uint64),
    ]
