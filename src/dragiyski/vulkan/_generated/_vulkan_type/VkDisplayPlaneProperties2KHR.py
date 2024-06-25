import ctypes

class VkDisplayPlaneProperties2KHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'displayPlaneProperties': VkDisplayPlanePropertiesKHR,
        }


from .VkDisplayPlanePropertiesKHR import VkDisplayPlanePropertiesKHR

VkDisplayPlaneProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayPlaneProperties', VkDisplayPlanePropertiesKHR),
]
