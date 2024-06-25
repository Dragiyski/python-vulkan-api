import ctypes

class VkRayTracingShaderGroupCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'type': ctypes.c_int,
            'generalShader': ctypes.c_uint32,
            'closestHitShader': ctypes.c_uint32,
            'anyHitShader': ctypes.c_uint32,
            'intersectionShader': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('type', ctypes.c_int),
        ('generalShader', ctypes.c_uint32),
        ('closestHitShader', ctypes.c_uint32),
        ('anyHitShader', ctypes.c_uint32),
        ('intersectionShader', ctypes.c_uint32),
    ]
