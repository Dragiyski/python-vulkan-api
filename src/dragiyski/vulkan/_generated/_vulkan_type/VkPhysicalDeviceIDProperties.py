import ctypes

class VkPhysicalDeviceIDProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'deviceUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
            'driverUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
            'deviceLUID': ctypes.ARRAY(ctypes.c_uint8, 8),
            'deviceNodeMask': ctypes.c_uint32,
            'deviceLUIDValid': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('driverUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('deviceLUID', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('deviceNodeMask', ctypes.c_uint32),
        ('deviceLUIDValid', ctypes.c_uint32),
    ]
