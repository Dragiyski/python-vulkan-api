import ctypes

class VkImageCompressionControlEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'compressionControlPlaneCount': ctypes.c_uint32,
            'pFixedRateFlags': ctypes.POINTER(ctypes.c_uint32),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('compressionControlPlaneCount', ctypes.c_uint32),
        ('pFixedRateFlags', ctypes.POINTER(ctypes.c_uint32)),
    ]
