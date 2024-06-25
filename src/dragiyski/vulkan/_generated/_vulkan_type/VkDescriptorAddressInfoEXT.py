import ctypes

class VkDescriptorAddressInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'address': ctypes.c_uint64,
            'range': ctypes.c_uint64,
            'format': ctypes.c_int,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('address', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
        ('format', ctypes.c_int),
    ]
