import ctypes

class VkLayerSettingEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'pLayerName': ctypes.c_char_p,
            'pSettingName': ctypes.c_char_p,
            'type': ctypes.c_int,
            'valueCount': ctypes.c_uint32,
            'pValues': ctypes.c_void_p,
        }

    _fields_ = [
        ('pLayerName', ctypes.c_char_p),
        ('pSettingName', ctypes.c_char_p),
        ('type', ctypes.c_int),
        ('valueCount', ctypes.c_uint32),
        ('pValues', ctypes.c_void_p),
    ]
