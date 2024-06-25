import ctypes

class VkDisplayModeProperties2KHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'displayModeProperties': VkDisplayModePropertiesKHR,
        }


from .VkDisplayModePropertiesKHR import VkDisplayModePropertiesKHR

VkDisplayModeProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayModeProperties', VkDisplayModePropertiesKHR),
]
