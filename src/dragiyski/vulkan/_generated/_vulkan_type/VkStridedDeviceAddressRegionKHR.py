import ctypes

class VkStridedDeviceAddressRegionKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'deviceAddress': ctypes.c_uint64,
            'stride': ctypes.c_uint64,
            'size': ctypes.c_uint64,
        }

    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('stride', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]
