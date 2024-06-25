import ctypes

class VkPipelinePropertiesIdentifierEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pipelineIdentifier': ctypes.ARRAY(ctypes.c_uint8, 16),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]
