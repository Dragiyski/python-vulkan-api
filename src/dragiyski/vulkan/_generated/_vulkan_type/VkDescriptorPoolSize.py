import ctypes

class VkDescriptorPoolSize(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'type': ctypes.c_int,
            'descriptorCount': ctypes.c_uint32,
        }

    _fields_ = [
        ('type', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
    ]
