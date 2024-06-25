import ctypes

class VkPipelineCreationFeedback(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': ctypes.c_uint32,
            'duration': ctypes.c_uint64,
        }

    _fields_ = [
        ('flags', ctypes.c_uint32),
        ('duration', ctypes.c_uint64),
    ]
