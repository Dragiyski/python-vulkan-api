import ctypes

class VkPushConstantsInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'layout': ctypes.c_void_p,
            'stageFlags': ctypes.c_uint32,
            'offset': ctypes.c_uint32,
            'size': ctypes.c_uint32,
            'pValues': ctypes.c_void_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('layout', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
        ('pValues', ctypes.c_void_p),
    ]
