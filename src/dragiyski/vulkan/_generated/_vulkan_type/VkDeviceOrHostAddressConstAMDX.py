import ctypes

class VkDeviceOrHostAddressConstAMDX(ctypes.Union):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'deviceAddress': ctypes.c_uint64,
            'hostAddress': ctypes.c_void_p,
        }

    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('hostAddress', ctypes.c_void_p),
    ]
