import ctypes

class VkSurfaceFormat2KHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'surfaceFormat': VkSurfaceFormatKHR,
        }


from .VkSurfaceFormatKHR import VkSurfaceFormatKHR

VkSurfaceFormat2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceFormat', VkSurfaceFormatKHR),
]
