import ctypes

class VkPhysicalDeviceMultiviewFeatures(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'multiview': ctypes.c_uint32,
            'multiviewGeometryShader': ctypes.c_uint32,
            'multiviewTessellationShader': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multiview', ctypes.c_uint32),
        ('multiviewGeometryShader', ctypes.c_uint32),
        ('multiviewTessellationShader', ctypes.c_uint32),
    ]
