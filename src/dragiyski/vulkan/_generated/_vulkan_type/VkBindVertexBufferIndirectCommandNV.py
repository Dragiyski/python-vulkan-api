import ctypes

class VkBindVertexBufferIndirectCommandNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'bufferAddress': ctypes.c_uint64,
            'size': ctypes.c_uint32,
            'stride': ctypes.c_uint32,
        }

    _fields_ = [
        ('bufferAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
    ]
