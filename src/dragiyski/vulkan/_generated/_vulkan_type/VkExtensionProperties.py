import ctypes

class VkExtensionProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'extensionName': ctypes.ARRAY(ctypes.c_char, 256),
            'specVersion': ctypes.c_uint32,
        }

    _fields_ = [
        ('extensionName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
    ]
