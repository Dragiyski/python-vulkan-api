import ctypes

class VkDescriptorImageInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sampler': ctypes.c_void_p,
            'imageView': ctypes.c_void_p,
            'imageLayout': ctypes.c_int,
        }

    _fields_ = [
        ('sampler', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('imageLayout', ctypes.c_int),
    ]
