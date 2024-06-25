import ctypes

class VkShaderModuleIdentifierEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'identifierSize': ctypes.c_uint32,
            'identifier': ctypes.ARRAY(ctypes.c_uint8, 32),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('identifierSize', ctypes.c_uint32),
        ('identifier', ctypes.ARRAY(ctypes.c_uint8, 32)),
    ]
