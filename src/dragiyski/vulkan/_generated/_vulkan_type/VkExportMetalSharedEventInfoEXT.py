import ctypes

class VkExportMetalSharedEventInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'semaphore': ctypes.c_void_p,
            'event': ctypes.c_void_p,
            'mtlSharedEvent': ctypes.c_void_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('event', ctypes.c_void_p),
        ('mtlSharedEvent', ctypes.c_void_p),
    ]
