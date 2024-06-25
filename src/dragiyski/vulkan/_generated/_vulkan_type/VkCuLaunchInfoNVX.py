import ctypes

class VkCuLaunchInfoNVX(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'function': ctypes.c_void_p,
            'gridDimX': ctypes.c_uint32,
            'gridDimY': ctypes.c_uint32,
            'gridDimZ': ctypes.c_uint32,
            'blockDimX': ctypes.c_uint32,
            'blockDimY': ctypes.c_uint32,
            'blockDimZ': ctypes.c_uint32,
            'sharedMemBytes': ctypes.c_uint32,
            'paramCount': ctypes.c_size_t,
            'pParams': ctypes.POINTER(ctypes.c_void_p),
            'extraCount': ctypes.c_size_t,
            'pExtras': ctypes.POINTER(ctypes.c_void_p),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('function', ctypes.c_void_p),
        ('gridDimX', ctypes.c_uint32),
        ('gridDimY', ctypes.c_uint32),
        ('gridDimZ', ctypes.c_uint32),
        ('blockDimX', ctypes.c_uint32),
        ('blockDimY', ctypes.c_uint32),
        ('blockDimZ', ctypes.c_uint32),
        ('sharedMemBytes', ctypes.c_uint32),
        ('paramCount', ctypes.c_size_t),
        ('pParams', ctypes.POINTER(ctypes.c_void_p)),
        ('extraCount', ctypes.c_size_t),
        ('pExtras', ctypes.POINTER(ctypes.c_void_p)),
    ]
