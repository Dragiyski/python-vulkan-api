import ctypes

class VkDrmFormatModifierPropertiesList2EXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'drmFormatModifierCount': ctypes.c_uint32,
            'pDrmFormatModifierProperties': ctypes.POINTER(VkDrmFormatModifierProperties2EXT),
        }


from .VkDrmFormatModifierProperties2EXT import VkDrmFormatModifierProperties2EXT

VkDrmFormatModifierPropertiesList2EXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierProperties2EXT)),
]
