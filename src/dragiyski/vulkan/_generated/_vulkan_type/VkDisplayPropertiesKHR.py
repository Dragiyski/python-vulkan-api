import ctypes

class VkDisplayPropertiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'display': ctypes.c_void_p,
            'displayName': ctypes.c_char_p,
            'physicalDimensions': VkExtent2D,
            'physicalResolution': VkExtent2D,
            'supportedTransforms': ctypes.c_uint32,
            'planeReorderPossible': ctypes.c_uint32,
            'persistentContent': ctypes.c_uint32,
        }


from .VkExtent2D import VkExtent2D

VkDisplayPropertiesKHR._fields_ = [
    ('display', ctypes.c_void_p),
    ('displayName', ctypes.c_char_p),
    ('physicalDimensions', VkExtent2D),
    ('physicalResolution', VkExtent2D),
    ('supportedTransforms', ctypes.c_uint32),
    ('planeReorderPossible', ctypes.c_uint32),
    ('persistentContent', ctypes.c_uint32),
]
