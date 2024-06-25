import ctypes

class VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'fragmentShaderSampleInterlock': ctypes.c_uint32,
            'fragmentShaderPixelInterlock': ctypes.c_uint32,
            'fragmentShaderShadingRateInterlock': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentShaderSampleInterlock', ctypes.c_uint32),
        ('fragmentShaderPixelInterlock', ctypes.c_uint32),
        ('fragmentShaderShadingRateInterlock', ctypes.c_uint32),
    ]
