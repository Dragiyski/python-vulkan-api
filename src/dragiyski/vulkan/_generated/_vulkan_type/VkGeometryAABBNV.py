import ctypes

class VkGeometryAABBNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'aabbData': ctypes.c_void_p,
            'numAABBs': ctypes.c_uint32,
            'stride': ctypes.c_uint32,
            'offset': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('aabbData', ctypes.c_void_p),
        ('numAABBs', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('offset', ctypes.c_uint64),
    ]
