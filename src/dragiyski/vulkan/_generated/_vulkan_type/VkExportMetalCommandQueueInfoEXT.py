import ctypes

class VkExportMetalCommandQueueInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'queue': ctypes.c_void_p,
            'mtlCommandQueue': ctypes.c_void_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queue', ctypes.c_void_p),
        ('mtlCommandQueue', ctypes.c_void_p),
    ]
