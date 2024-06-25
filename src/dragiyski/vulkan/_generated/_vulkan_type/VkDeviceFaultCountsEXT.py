import ctypes

class VkDeviceFaultCountsEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'addressInfoCount': ctypes.c_uint32,
            'vendorInfoCount': ctypes.c_uint32,
            'vendorBinarySize': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('addressInfoCount', ctypes.c_uint32),
        ('vendorInfoCount', ctypes.c_uint32),
        ('vendorBinarySize', ctypes.c_uint64),
    ]
