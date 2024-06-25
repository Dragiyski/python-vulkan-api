import ctypes

class VkPipelineExecutableInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pipeline': ctypes.c_void_p,
            'executableIndex': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipeline', ctypes.c_void_p),
        ('executableIndex', ctypes.c_uint32),
    ]
