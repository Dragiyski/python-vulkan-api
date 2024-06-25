import ctypes

class VkQueueFamilyProperties2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'queueFamilyProperties': VkQueueFamilyProperties,
        }


from .VkQueueFamilyProperties import VkQueueFamilyProperties

VkQueueFamilyProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('queueFamilyProperties', VkQueueFamilyProperties),
]
