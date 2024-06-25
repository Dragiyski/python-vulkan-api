import ctypes

class VkMultisamplePropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'maxSampleLocationGridSize': VkExtent2D,
        }


from .VkExtent2D import VkExtent2D

VkMultisamplePropertiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxSampleLocationGridSize', VkExtent2D),
]
