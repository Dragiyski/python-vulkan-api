import ctypes

class VkDrmFormatModifierPropertiesListEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'drmFormatModifierCount': ctypes.c_uint32,
            'pDrmFormatModifierProperties': ctypes.POINTER(VkDrmFormatModifierPropertiesEXT),
        }


from .VkDrmFormatModifierPropertiesEXT import VkDrmFormatModifierPropertiesEXT

VkDrmFormatModifierPropertiesListEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierPropertiesEXT)),
]
