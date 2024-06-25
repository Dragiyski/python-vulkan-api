import ctypes

class VkVideoSessionParametersCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'videoSessionParametersTemplate': ctypes.c_void_p,
            'videoSession': ctypes.c_void_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('videoSessionParametersTemplate', ctypes.c_void_p),
        ('videoSession', ctypes.c_void_p),
    ]
