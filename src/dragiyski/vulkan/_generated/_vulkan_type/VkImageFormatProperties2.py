import ctypes

class VkImageFormatProperties2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'imageFormatProperties': VkImageFormatProperties,
        }


from .VkImageFormatProperties import VkImageFormatProperties

VkImageFormatProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageFormatProperties', VkImageFormatProperties),
]
