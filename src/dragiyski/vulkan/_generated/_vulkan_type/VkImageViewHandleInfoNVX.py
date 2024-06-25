import ctypes

class VkImageViewHandleInfoNVX(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'imageView': ctypes.c_void_p,
            'descriptorType': ctypes.c_int,
            'sampler': ctypes.c_void_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('descriptorType', ctypes.c_int),
        ('sampler', ctypes.c_void_p),
    ]
