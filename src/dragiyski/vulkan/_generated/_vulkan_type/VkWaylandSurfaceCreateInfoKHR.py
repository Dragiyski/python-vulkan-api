import ctypes

class VkWaylandSurfaceCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'display': ctypes.c_void_p,
            'surface': ctypes.c_void_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('display', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]
