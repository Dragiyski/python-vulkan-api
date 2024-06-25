import ctypes

class VkDisplaySurfaceCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'displayMode': ctypes.c_void_p,
            'planeIndex': ctypes.c_uint32,
            'planeStackIndex': ctypes.c_uint32,
            'transform': ctypes.c_uint32,
            'globalAlpha': ctypes.c_float,
            'alphaMode': ctypes.c_uint32,
            'imageExtent': VkExtent2D,
        }


from .VkExtent2D import VkExtent2D

VkDisplaySurfaceCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('displayMode', ctypes.c_void_p),
    ('planeIndex', ctypes.c_uint32),
    ('planeStackIndex', ctypes.c_uint32),
    ('transform', ctypes.c_uint32),
    ('globalAlpha', ctypes.c_float),
    ('alphaMode', ctypes.c_uint32),
    ('imageExtent', VkExtent2D),
]
