import ctypes

class VkDescriptorSetLayoutBinding(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'binding': ctypes.c_uint32,
            'descriptorType': ctypes.c_int,
            'descriptorCount': ctypes.c_uint32,
            'stageFlags': ctypes.c_uint32,
            'pImmutableSamplers': ctypes.POINTER(ctypes.c_void_p),
        }

    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('descriptorType', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
        ('stageFlags', ctypes.c_uint32),
        ('pImmutableSamplers', ctypes.POINTER(ctypes.c_void_p)),
    ]
