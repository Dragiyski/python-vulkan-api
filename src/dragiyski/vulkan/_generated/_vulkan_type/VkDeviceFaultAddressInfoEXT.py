import ctypes

class VkDeviceFaultAddressInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'addressType': ctypes.c_int,
            'reportedAddress': ctypes.c_uint64,
            'addressPrecision': ctypes.c_uint64,
        }

    _fields_ = [
        ('addressType', ctypes.c_int),
        ('reportedAddress', ctypes.c_uint64),
        ('addressPrecision', ctypes.c_uint64),
    ]
