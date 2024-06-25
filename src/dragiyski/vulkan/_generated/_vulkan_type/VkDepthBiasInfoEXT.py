import ctypes

class VkDepthBiasInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'depthBiasConstantFactor': ctypes.c_float,
            'depthBiasClamp': ctypes.c_float,
            'depthBiasSlopeFactor': ctypes.c_float,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasConstantFactor', ctypes.c_float),
        ('depthBiasClamp', ctypes.c_float),
        ('depthBiasSlopeFactor', ctypes.c_float),
    ]
