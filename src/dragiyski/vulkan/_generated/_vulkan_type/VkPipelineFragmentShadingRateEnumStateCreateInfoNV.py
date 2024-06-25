import ctypes

class VkPipelineFragmentShadingRateEnumStateCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'shadingRateType': ctypes.c_int,
            'shadingRate': ctypes.c_int,
            'combinerOps': ctypes.ARRAY(ctypes.c_int, 2),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shadingRateType', ctypes.c_int),
        ('shadingRate', ctypes.c_int),
        ('combinerOps', ctypes.ARRAY(ctypes.c_int, 2)),
    ]
