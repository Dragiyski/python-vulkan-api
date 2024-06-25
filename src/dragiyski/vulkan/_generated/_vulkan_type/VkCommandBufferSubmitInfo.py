import ctypes

class VkCommandBufferSubmitInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'commandBuffer': ctypes.c_void_p,
            'deviceMask': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandBuffer', ctypes.c_void_p),
        ('deviceMask', ctypes.c_uint32),
    ]
