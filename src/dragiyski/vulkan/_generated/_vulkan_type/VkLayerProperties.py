import ctypes

class VkLayerProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'layerName': ctypes.ARRAY(ctypes.c_char, 256),
            'specVersion': ctypes.c_uint32,
            'implementationVersion': ctypes.c_uint32,
            'description': ctypes.ARRAY(ctypes.c_char, 256),
        }

    _fields_ = [
        ('layerName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
        ('implementationVersion', ctypes.c_uint32),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ]
