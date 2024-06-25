import ctypes

class VkCooperativeMatrixPropertiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'MSize': ctypes.c_uint32,
            'NSize': ctypes.c_uint32,
            'KSize': ctypes.c_uint32,
            'AType': ctypes.c_int,
            'BType': ctypes.c_int,
            'CType': ctypes.c_int,
            'ResultType': ctypes.c_int,
            'saturatingAccumulation': ctypes.c_uint32,
            'scope': ctypes.c_int,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('MSize', ctypes.c_uint32),
        ('NSize', ctypes.c_uint32),
        ('KSize', ctypes.c_uint32),
        ('AType', ctypes.c_int),
        ('BType', ctypes.c_int),
        ('CType', ctypes.c_int),
        ('ResultType', ctypes.c_int),
        ('saturatingAccumulation', ctypes.c_uint32),
        ('scope', ctypes.c_int),
    ]
