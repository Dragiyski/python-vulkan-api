import ctypes

class VkPipelineShaderStageModuleIdentifierCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'identifierSize': ctypes.c_uint32,
            'pIdentifier': ctypes.POINTER(ctypes.c_uint8),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('identifierSize', ctypes.c_uint32),
        ('pIdentifier', ctypes.POINTER(ctypes.c_uint8)),
    ]
