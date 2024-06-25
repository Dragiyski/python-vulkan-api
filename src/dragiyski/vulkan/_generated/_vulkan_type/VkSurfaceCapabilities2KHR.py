import ctypes

class VkSurfaceCapabilities2KHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'surfaceCapabilities': VkSurfaceCapabilitiesKHR,
        }


from .VkSurfaceCapabilitiesKHR import VkSurfaceCapabilitiesKHR

VkSurfaceCapabilities2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceCapabilities', VkSurfaceCapabilitiesKHR),
]
