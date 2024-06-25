import ctypes

class VkDisplayProperties2KHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'displayProperties': VkDisplayPropertiesKHR,
        }


from .VkDisplayPropertiesKHR import VkDisplayPropertiesKHR

VkDisplayProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayProperties', VkDisplayPropertiesKHR),
]
