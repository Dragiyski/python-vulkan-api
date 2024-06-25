import ctypes

class VkExternalImageFormatProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'externalMemoryProperties': VkExternalMemoryProperties,
        }


from .VkExternalMemoryProperties import VkExternalMemoryProperties

VkExternalImageFormatProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('externalMemoryProperties', VkExternalMemoryProperties),
]
