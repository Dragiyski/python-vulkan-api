import ctypes

class VkCopyAccelerationStructureInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'src': ctypes.c_void_p,
            'dst': ctypes.c_void_p,
            'mode': ctypes.c_int,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('src', ctypes.c_void_p),
        ('dst', ctypes.c_void_p),
        ('mode', ctypes.c_int),
    ]
