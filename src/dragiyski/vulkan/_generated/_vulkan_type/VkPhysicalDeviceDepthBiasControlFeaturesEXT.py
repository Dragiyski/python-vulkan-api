import ctypes

class VkPhysicalDeviceDepthBiasControlFeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'depthBiasControl': ctypes.c_uint32,
            'leastRepresentableValueForceUnormRepresentation': ctypes.c_uint32,
            'floatRepresentation': ctypes.c_uint32,
            'depthBiasExact': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasControl', ctypes.c_uint32),
        ('leastRepresentableValueForceUnormRepresentation', ctypes.c_uint32),
        ('floatRepresentation', ctypes.c_uint32),
        ('depthBiasExact', ctypes.c_uint32),
    ]
